/* Morrow Care: original, local-only UI demonstration. No network requests. */
const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const icon = (name, className = '') => `<svg class="${className}" aria-hidden="true"><use href="#i-${name}"/></svg>`;
const providers = { maya: { name: 'Dr. Maya Chen', initials: 'MC', className: 'doctor' }, jordan: { name: 'Dr. Jordan Lee', initials: 'JL', className: 'jordan' } };
const initialAppointments = [
  { id: 'a1', provider: 'maya', date: '2026-10-15', time: '10:30', type: 'Follow-up conversation', status: 'upcoming' },
  { id: 'a0', provider: 'maya', date: '2026-10-09', time: '09:00', type: 'First conversation', status: 'past' }
];
const documents = [
  { id: 'd1', title: 'Your visit summary', date: '12 Oct 2026', author: 'Dr. Maya Chen', category: 'Visit notes', content: 'This fictional administrative summary records a completed introductory appointment on 9 October 2026. Your next conversation is scheduled for 15 October 2026 at 10:30 AM IST.', bullets: ['Visit format: video conversation', 'Follow-up: scheduled with Dr. Maya Chen', 'Your personal questions: bring them to your next visit'] },
  { id: 'd2', title: 'Getting ready for your follow-up', date: '12 Oct 2026', author: 'Morrow Care team', category: 'Visit preparation', content: 'A simple administrative checklist for the fictional upcoming visit. This sample does not contain a clinical plan or medical advice.', bullets: ['Check the appointment date and time', 'Keep your personal questions nearby', 'Find a comfortable, quiet place for your video conversation'] },
  { id: 'd3', title: 'Your care space, explained', date: '09 Oct 2026', author: 'Morrow Care team', category: 'Welcome guide', content: 'Morrow Care is a fictional patient portal created to demonstrate a thoughtful healthtech interface. All names, clinicians, documents and bookings are sample data.', bullets: ['Overview: your next appointment and visit note', 'Appointments: see sample visits and try the booking flow', 'Documents: preview or download fictional administrative notes'] }
];
let appointments = structuredClone(initialAppointments);
let filter = 'upcoming';
let nextId = 2;
let bookingToken = 0;
let toastTimer;
let lastTrigger;
const bookingDialog = $('#booking-dialog');
const detailDialog = $('#detail-dialog');
const originalBooking = $('#booking-content').innerHTML;
const dateParts = date => { const [year, month, day] = date.split('-').map(Number); return new Date(year, month - 1, day, 12); };
const shortDate = date => dateParts(date).toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' });
const timeLabel = time => { const [hour, minute] = time.split(':').map(Number); return `${hour % 12 || 12}:${String(minute).padStart(2, '0')} ${hour >= 12 ? 'PM' : 'AM'}`; };
function showToast(message) { clearTimeout(toastTimer); $('#toast').textContent = message; $('#toast').hidden = false; toastTimer = setTimeout(() => { $('#toast').hidden = true; }, 3500); }
function route(moveFocus = false) {
  const page = ['overview', 'appointments', 'documents'].includes(location.hash.slice(1)) ? location.hash.slice(1) : 'overview';
  $$('.view').forEach(view => { view.hidden = view.id !== `view-${page}`; });
  $$('[data-nav]').forEach(link => { if (link.dataset.nav === page) link.setAttribute('aria-current', 'page'); else link.removeAttribute('aria-current'); });
  $('#page-crumb').textContent = page[0].toUpperCase() + page.slice(1);
  document.title = `Morrow Care · ${$('#page-crumb').textContent}`;
  if (moveFocus) $('#main').focus({ preventScroll: true });
}
function documentRow(doc) { return `<button class="document-row" data-document="${doc.id}"><span class="file-icon">${icon('file')}</span><span><strong>${doc.title}</strong><small>${doc.author} · ${doc.date}</small></span><span class="file-tag">${doc.category}</span>${icon('arrow', 'row-arrow')}</button>`; }
function renderDocuments() {
  $('#recent-documents').innerHTML = documents.slice(0, 2).map(documentRow).join('');
  const query = $('#document-search').value.trim().toLowerCase();
  const matches = documents.filter(doc => `${doc.title} ${doc.author} ${doc.category}`.toLowerCase().includes(query));
  $('#all-documents').innerHTML = matches.length ? matches.map(documentRow).join('') : '<div class="empty-state"><h2>No documents found.</h2><p>Try “visit”, “follow-up” or clear your search.</p><button class="button secondary" id="clear-search">Clear search</button></div>';
  $('.search-control span').textContent = `${matches.length} document${matches.length === 1 ? '' : 's'}`;
}
function renderAppointments() {
  const matches = appointments.filter(a => filter === 'all' || a.status === filter).sort((a, b) => (a.date + a.time).localeCompare(b.date + b.time));
  $('#appointment-count').textContent = `${matches.length} visit${matches.length === 1 ? '' : 's'}`;
  $('#appointment-list').innerHTML = matches.length ? matches.map(a => {
    const provider = providers[a.provider];
    return `<article class="appointment-row"><div class="calendar-tile"><small>${dateParts(a.date).toLocaleDateString('en-GB', { month: 'short' }).toUpperCase()}</small><strong>${dateParts(a.date).getDate()}</strong></div><div><h2>${a.type}</h2><p>${provider.name} · Primary care</p><div class="row-meta"><span>${icon('clock')}${timeLabel(a.time)} IST · 25 min</span><span>${icon(a.status === 'past' ? 'check' : 'video')}${a.status === 'past' ? 'Completed' : 'Video visit'}</span></div></div><button class="button secondary" data-appointment-detail="${a.id}">View details${icon('arrow')}</button></article>`;
  }).join('') : '<div class="empty-state"><h2>A little room in your calendar.</h2><p>No upcoming visits in this demo. Choose a time when you’re ready.</p><button class="button primary" data-book>Book a visit</button></div>';
}
function openDialog(dialog, trigger) { lastTrigger = trigger || document.activeElement; dialog.showModal(); }
function openBooking(trigger) {
  bookingToken++;
  $('#booking-content').innerHTML = originalBooking;
  ['visit-date', 'visit-time'].forEach(name => $$(`input[name="${name}"]`, bookingDialog).forEach(input => input.setAttribute('aria-describedby', name === 'visit-date' ? 'date-error' : 'time-error')));
  openDialog(bookingDialog, trigger);
}
function showDetail(kicker, content, trigger) { $('#detail-kicker').textContent = kicker; $('#detail-content').innerHTML = content; openDialog(detailDialog, trigger); }
function appointmentDetails(id, trigger) {
  const a = appointments.find(item => item.id === id);
  if (!a) { showToast('This sample appointment was removed.'); return; }
  const provider = providers[a.provider];
  showDetail(a.status === 'past' ? 'A COMPLETED CONVERSATION' : 'YOUR NEXT CONVERSATION', `<h2 id="detail-heading">${a.type}</h2><div class="detail-meta"><span>${shortDate(a.date)} 2026</span><span>${timeLabel(a.time)} IST · 25 min</span></div><div class="provider"><span class="avatar ${provider.className}">${provider.initials}</span><span><strong>${provider.name}</strong><small>Primary care · Video visit</small></span></div><div class="detail-body"><div class="detail-callout">${a.status === 'past' ? 'This fictional visit is marked complete. You can find its administrative summary in Documents.' : 'This is a sample appointment. Video joining is not connected in this demo.'}</div>${a.status === 'past' ? '<button class="button primary" id="detail-documents">See visit documents' + icon('arrow') + '</button>' : '<button class="button secondary" data-cancel-request="' + a.id + '">Cancel this demo visit</button>'}</div>`, trigger);
}
function previewDocument(id, trigger) {
  const doc = documents.find(item => item.id === id);
  if (!doc) return;
  showDetail(doc.category.toUpperCase(), `<h2 id="detail-heading">${doc.title}</h2><div class="detail-meta"><span>${doc.author}</span><span>${doc.date}</span></div><div class="detail-body"><p>${doc.content}</p><h3>At a glance</h3><ul>${doc.bullets.map(item => `<li>${item}</li>`).join('')}</ul><div class="detail-callout">Fictional sample document. No medical advice or real patient information.</div><button class="button primary" data-download="${doc.id}">${icon('download')}Download sample note</button></div>`, trigger);
}
function updateBookingAvailability() {
  const form = $('#booking-form');
  if (!form) return;
  const provider = $('input[name="provider"]:checked', form)?.value;
  const date = $('input[name="visit-date"]:checked', form)?.value;
  $$('input[name="visit-time"]', form).forEach(input => {
    const taken = appointments.some(a => a.status === 'upcoming' && a.provider === provider && a.date === date && a.time === input.value);
    input.disabled = taken;
    input.nextElementSibling.textContent = `${timeLabel(input.value)}${taken ? ' · booked' : ''}`;
    if (taken) input.checked = false;
  });
}
document.addEventListener('click', event => {
  const button = event.target.closest('button');
  if (!button) return;
  if (button.matches('[data-book]')) openBooking(button);
  if (button.matches('.close-dialog')) button.closest('dialog').close();
  if (button.dataset.filter) {
    filter = button.dataset.filter;
    $$('[data-filter]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    renderAppointments();
  }
  if (button.dataset.appointmentDetail) appointmentDetails(button.dataset.appointmentDetail, button);
  if (button.dataset.document) previewDocument(button.dataset.document, button);
  if (button.dataset.download) {
    const doc = documents.find(item => item.id === button.dataset.download);
    const content = `MORROW CARE — FICTIONAL SAMPLE\n\n${doc.title}\n${doc.author} · ${doc.date}\n\n${doc.content}\n\n${doc.bullets.map(item => `• ${item}`).join('\n')}\n\nNo medical advice or real patient information.\n`;
    const url = URL.createObjectURL(new Blob([content], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a'); link.href = url; link.download = `morrow-care-${doc.id}-sample.txt`; link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000); showToast('Fictional note downloaded.');
  }
  if (button.dataset.cancelRequest) {
    const a = appointments.find(item => item.id === button.dataset.cancelRequest);
    $('#detail-content').innerHTML = `<h2 id="detail-heading">Cancel this sample visit?</h2><div class="detail-body"><p>${shortDate(a.date)} · ${timeLabel(a.time)} IST with ${providers[a.provider].name}.</p><p>This removes the appointment from the demo. You can book another time or reset the sample.</p><div class="dialog-actions"><button class="button secondary" data-keep-appointment="${a.id}">Keep visit</button><button class="button primary" data-confirm-cancel="${a.id}">Cancel demo visit</button></div></div>`;
    $('[data-keep-appointment]').focus();
  }
  if (button.dataset.keepAppointment) { const a = appointments.find(item => item.id === button.dataset.keepAppointment); detailDialog.close(); appointmentDetails(a.id, lastTrigger); }
  if (button.dataset.confirmCancel) {
    const id = button.dataset.confirmCancel;
    appointments = appointments.filter(a => a.id !== id); renderAppointments(); detailDialog.close();
    syncOverview();
    showToast('Sample visit canceled. You can choose another time.');
  }
  if (button.id === 'detail-documents') { detailDialog.close(); location.hash = 'documents'; }
  if (button.id === 'confirmation-appointments') { bookingDialog.close(); filter = 'upcoming'; $$('[data-filter]').forEach(item => item.setAttribute('aria-pressed', String(item.dataset.filter === filter))); renderAppointments(); location.hash = 'appointments'; }
  if (button.id === 'clear-search') { $('#document-search').value = ''; renderDocuments(); $('#document-search').focus(); }
  if (button.id === 'save-note') { const note = $('#visit-note').value.trim(); $('#note-status').textContent = note ? 'Saved for this demo session' : 'Your note is empty'; showToast(note ? 'Your visit note is saved in this session.' : 'Add a question before saving your note.'); if (!note) $('#visit-note').focus(); }
  if (button.id === 'help-open') showDetail('A DESIGN YOU CAN TRY', '<h2 id="detail-heading">Welcome to Morrow.</h2><div class="detail-body"><p>This original healthtech portal is an interactive design sample with fictional people and records.</p><h3>Try a few things</h3><ul><li>Book a visit with a provider, day and time.</li><li>Switch between upcoming and past appointments.</li><li>Cancel a sample booking or preview a document.</li><li>Save a personal visit note, then reset the demo.</li></ul><div class="detail-callout">Nothing is sent to a clinician. There is no backend, login, payment or medical guidance. Demo changes last until reload or reset.</div></div>', button);
  if (button.id === 'profile-open') showDetail('FICTIONAL PERSONAL ACCOUNT', '<h2 id="detail-heading">Hello, Alex.</h2><div class="detail-body"><p>Alex Morgan is a fictional patient created for this interface sample. No sign-in or real account is connected.</p><div class="detail-callout">Your care space is set to India Standard Time (IST). All dates are fixed sample dates in October 2026.</div></div>', button);
  if (button.id === 'reset-demo') {
    appointments = structuredClone(initialAppointments); nextId = 2; filter = 'upcoming'; $('#visit-note').value = ''; $('#note-status').textContent = 'Kept only in this demo session'; $('#document-search').value = '';
    $$('[data-filter]').forEach(item => item.setAttribute('aria-pressed', String(item.dataset.filter === filter)));
    restoreOverview(); restoreJourney(); renderAppointments(); renderDocuments(); showToast('Demo reset. You’re back to the original sample.');
  }
});
const originalHero = $('.appointment-hero').innerHTML;
const originalJourney = $('.journey-rail').innerHTML;
function restoreOverview() { $('.appointment-hero').innerHTML = originalHero; }
function restoreJourney() { $('.journey-rail').innerHTML = originalJourney; }
function syncOverview() {
  const next = appointments.filter(a => a.status === 'upcoming').sort((a, b) => (a.date + a.time).localeCompare(b.date + b.time))[0];
  restoreJourney();
  if (!next) {
    $('.appointment-hero').innerHTML = '<div class="hero-kicker"><span class="status-pill">A little room in your calendar</span></div><div class="hero-body"><div class="hero-copy"><h2>Find your<br>next conversation.</h2><p>Your original demo follow-up was canceled.</p></div></div><div class="hero-footer"><span>Choose another sample date when you’re ready.</span><button class="button hero-button" data-book>Book a visit' + icon('arrow') + '</button></div>';
    $('.journey-rail .current .step-date').textContent = 'WHEN YOU’RE READY';
    $('.journey-rail .current strong').textContent = 'Choose your next time';
    $('.journey-rail .current small').textContent = 'No visit scheduled';
    return;
  }
  restoreOverview();
  if (next.id === 'a1') return;
  const provider = providers[next.provider];
  $('.hero-copy>p').textContent = `Your visit with ${provider.name}.`;
  $('.appointment-details').innerHTML = `<span>${icon('calendar')}${shortDate(next.date)}</span><span>${icon('clock')}${timeLabel(next.time)} · 25 min</span>`;
  $('.appointment-hero .provider').innerHTML = `<span class="avatar ${provider.className}">${provider.initials}</span><span><strong>${provider.name}</strong><small>Primary care · Video visit</small></span>`;
  $('.hero-button').dataset.appointmentDetail = next.id;
  $('.journey-rail .current .step-date').textContent = dateParts(next.date).toLocaleDateString('en-GB', { day: '2-digit', month: 'short' }).toUpperCase();
  $('.journey-rail .current strong').textContent = 'Your next conversation';
}
bookingDialog.addEventListener('change', event => {
  if (!event.target.matches('input[type="radio"]')) return;
  const input = event.target;
  if (input.name === 'visit-date' || input.name === 'visit-time') {
    const error = input.name === 'visit-date' ? $('#date-error') : $('#time-error'); error.hidden = true;
    $$(`input[name="${input.name}"]`, bookingDialog).forEach(radio => radio.removeAttribute('aria-invalid'));
  }
  $('#booking-error').hidden = true;
  updateBookingAvailability();
});
bookingDialog.addEventListener('submit', event => {
  if (event.target.id !== 'booking-form') return;
  event.preventDefault();
  const form = event.target;
  const provider = $('input[name="provider"]:checked', form)?.value;
  const date = $('input[name="visit-date"]:checked', form)?.value;
  const time = $('input[name="visit-time"]:checked', form)?.value;
  let firstError;
  [['visit-date', date, 'date-error'], ['visit-time', time, 'time-error']].forEach(([name, value, errorId]) => {
    $('#' + errorId).hidden = Boolean(value);
    $$(`input[name="${name}"]`, form).forEach(input => value ? input.removeAttribute('aria-invalid') : input.setAttribute('aria-invalid', 'true'));
    if (!value && !firstError) firstError = $(`input[name="${name}"]:not(:disabled)`, form);
  });
  if (firstError) { firstError.focus(); return; }
  if (appointments.some(a => a.status === 'upcoming' && a.provider === provider && a.date === date && a.time === time)) { $('#booking-error').textContent = 'This time is already booked in your demo. Choose another available time.'; $('#booking-error').hidden = false; updateBookingAvailability(); return; }
  const submit = $('#booking-submit'); submit.disabled = true; submit.textContent = 'Saving sample visit…'; form.setAttribute('aria-busy', 'true');
  $$('input', form).forEach(input => { input.disabled = true; });
  const token = ++bookingToken;
  setTimeout(() => {
    if (token !== bookingToken || !bookingDialog.open) return;
    appointments.push({ id: 'a' + nextId++, provider, date, time, type: 'A new conversation', status: 'upcoming' });
    renderAppointments(); syncOverview();
    $('#booking-content').innerHTML = `<div class="success-symbol">${icon('check')}</div><h2 id="booking-heading" tabindex="-1">You’re on the calendar.</h2><p class="dialog-intro">A little time set aside, just for you.</p><div class="success-details"><strong>${providers[provider].name}</strong><p>${shortDate(date)} 2026 · ${timeLabel(time)} IST</p><p>25-minute video visit</p></div><div class="detail-callout">This sample appointment is saved only in your current demo session. No provider has been contacted.</div><div class="dialog-actions"><button class="button secondary close-dialog">Done</button><button class="button primary" id="confirmation-appointments">See appointments${icon('arrow')}</button></div>`;
    $('#booking-heading').focus();
  }, 650);
});
for (const dialog of [bookingDialog, detailDialog]) {
  dialog.addEventListener('close', () => { if (dialog === bookingDialog) bookingToken++; if (lastTrigger?.isConnected) lastTrigger.focus({ preventScroll: true }); });
  dialog.addEventListener('click', event => { if (event.target !== dialog) return; const rect = dialog.getBoundingClientRect(); if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close(); });
}
$('#document-search').addEventListener('input', renderDocuments);
$('#visit-note').addEventListener('input', () => { $('#note-status').textContent = 'Unsaved changes · session only'; });
window.addEventListener('hashchange', () => route(true));
renderDocuments(); renderAppointments(); route();
