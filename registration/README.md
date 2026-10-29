# Registration (LimeSurvey)

Live survey: <https://limesurvey.imis.uni-luebeck.de/index.php/269832?lang=de> (ID 269832). The
"Jetzt anmelden" button in `../site/index.html` links here.

| File | Purpose |
|---|---|
| `build_survey.py` | Source of the form: questions, settings and all texts. Run `python3 registration/build_survey.py` after changing it. |
| `anmeldung.tsv` | Generated. The whole form as a LimeSurvey import file. |
| `texte.md` | Generated. The texts as copy-and-paste blocks, for updating the live survey without re-importing. |

The import file was tested against a local LimeSurvey 6.17.18. The test covered the requested survey
ID, import, activation, the privacy checkbox, email validation, encrypted storage and the
confirmation email. The IMIS instance also runs LimeSurvey 6.

## Updating the live survey

The live survey was imported from an earlier version of the file. To bring it up to date, paste the
blocks from `texte.md` into the fields named there. Texts can be changed while the survey is
active, and existing responses are kept. Questions, however, are locked while it is active.

Delete any test registrations before the link goes public. Places are given out in order of
submission, so a test entry would take one of the 12.

## Setting it up from scratch (e.g. for a later workshop)

1. **Import:** *Create survey → Import* and choose `anmeldung.tsv`.
2. **Check the survey ID.** The file requests ID 269832. LimeSurvey keeps it only if no survey with
   that ID exists; otherwise it silently assigns a random one. Update the link in
   `../site/index.html` to match.
3. **Fill in the placeholders:** search the texts for `[[TODO:`.
4. **Check settings the file leaves to your instance:**
   - *General settings → Administrator / Admin email.*
   - *Publication & access → Expiry date* (registration deadline).
   - Optional: get an email for every registration. Put your own address in *Notifications & data →
     Send basic admin notification email to*.
   - Optional: a hard cap via *Quotas*. Without one, places go first come, first served by submission
     time, and later registrations form the waiting list.
5. **Activate** in *open access mode* (no participant list).
6. **Test once with your own address.** Check that the confirmation email arrives and isn't marked
   as spam. Then delete the test response, so it doesn't take a place.

## Questions

| Code | Question | Type | Required | Encrypted |
|---|---|---|---|---|
| VORNAME | Vorname | short text | yes | yes |
| NACHNAME | Nachname | short text | yes | yes |
| EMAIL | E-Mail-Adresse (format validated) | short text | yes | yes |
| EINRICHTUNG | Institut, Klinik oder Einrichtung | short text | yes | no |
| POSITION | Promotion / Postdoc / Professur / Wiss. Mitarbeit / Sonstiges | list | yes | no |
| OS | macOS / Windows / Linux | list | yes | no |
| ERFAHRUNG | Use of generative AI so far (selten … täglich) | list | yes | no |
| CLAUDE | Paid Claude access (ja / richte ich ein / unklar) | list | yes | no |
| VORHABEN | A research task to try with agentic AI | long text | no | yes |

## Privacy

- **Legal basis** follows the IMIS *Datenschutzinformation für Veranstaltungsmanagement*:
  - required fields: Art. 6(1)(b) GDPR, plus Art. 6(1)(e) with § 3 of the Schleswig-Holstein
    Higher Education Act (Hochschulgesetz);
  - the voluntary field: Art. 6(1)(f), legitimate interest.

  Because none of this rests on consent, the checkbox only confirms that the notice was read ("zur
  Kenntnis genommen"); it is not a consent. The notice links to the IMIS privacy pages for details.
- **Retention:** the notice promises deletion at the latest three months after the workshop.
- **Data stored.** No IP address, referrer URL or page timings are stored with the response. The
  web server's own access logs are outside the survey's control, so check them with your IT. The
  submission time is kept because places are given out in order of registration.
- **Encryption.** Name, email address and the free-text answer are encrypted in the database.
  Exports and the response view show them decrypted. Server administrators can still read them.
- **Confirmation email.** LimeSurvey's own "confirmation email" only works for surveys with a
  participant list. This form instead sends the *detailed admin notification* to `{EMAIL}`, the
  address the participant entered, with participant-facing text. Don't add your own address to that
  field, or you'll receive the participant version; use the basic notification instead.
- **Deleting data** when the retention period ends: delete the responses, then the survey.
  Deactivating a survey alone does not delete anything. LimeSurvey keeps the responses as an
  archived table.
