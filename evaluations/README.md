# Behavioral evaluation cases

[cases.json](cases.json) provides realistic requests and observable expectations for future skill evaluations. They were reviewed as instruction/route cases during repository construction; they have **not** been independently executed across every AI host or model.

To evaluate a skill, give another session the case's request, necessary fictional source fixture and the selected skill folder. Observe the actual questions, output status, source handling, artifacts and validation claims. Do not tell it the expected answer when you want an independent test. Record what happened and make a narrow correction for a demonstrated failure.

Some hosts lack generation, rendering or audio listening. A truthful handoff is the correct result for those missing capabilities, not a failed demand to fabricate an artifact. Paid calls, external publication and private source access require authorization consistent with the real task.

Do not interpret a score or a passing metadata check as a guarantee of creative judgment. Compare real artifacts and their source fidelity, hierarchy, continuity and usability.
