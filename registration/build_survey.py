"""Generate the workshop registration survey: anmeldung.tsv (LimeSurvey import) and texte.md (copy and paste).

Run: python3 registration/build_survey.py

Format follows TSVImportSurvey() in LimeSurvey's application/helpers/admin/import_helper.php:
row order is structure (Q attaches to the last G, A to the last Q). No tabs, newlines or ASCII double
quotes inside cells; in HTML use single quotes for attributes.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "anmeldung.tsv")
TEXTS = os.path.join(HERE, "texte.md")
LANG = "de"
COLS = ["id", "related_id", "class", "type/scale", "name", "relevance", "text", "help",
        "language", "validation", "mandatory", "encrypted", "other", "default", "same_default"]

rows = []


def row(cls, **kw):
    r = {c: "" for c in COLS}
    r["class"] = cls
    for k, v in kw.items():
        r[k.replace("type_scale", "type/scale")] = v
    rows.append(r)


def S(name, value):
    row("S", name=name, text=value)


def SL(name, value):
    row("SL", name=name, text=value, language=LANG)


def G(name, text=""):
    row("G", name=name, text=text, language=LANG, relevance="1")


def Q(qtype, code, text, help="", mandatory="Y", encrypted="N", validation="", other="N"):
    row("Q", type_scale=qtype, name=code, text=text, help=help, language=LANG, relevance="1",
        mandatory=mandatory, encrypted=encrypted, validation=validation, other=other)


def A(code, text):
    row("A", type_scale="0", name=code, text=text, language=LANG)


# --- Survey settings (data minimisation: no IP, no referrer, no timings; datestamp kept for first-come order)
# ID of the live survey; a re-import gets it back only if that survey was deleted first, otherwise a random one.
S("sid", "269832")
S("language", LANG)
S("format", "A")
S("anonymized", "N")
S("datestamp", "Y")
S("ipaddr", "N")
S("refurl", "N")
S("savetimings", "N")
S("allowsave", "N")
S("usecookie", "N")
S("listpublic", "N")
S("publicstatistics", "N")
S("publicgraphs", "N")
S("printanswers", "N")
S("alloweditaftercompletion", "N")
S("sendconfirmation", "N")
S("assessments", "N")
S("showwelcome", "Y")
S("showprogress", "N")
S("showxquestions", "N")
S("shownoanswer", "N")
S("showqnumcode", "X")
S("showsurveypolicynotice", "2")
S("htmlemail", "Y")
S("emailresponseto", "{EMAIL}")

# --- Language settings
TITLE = "Einführung in agentische KI für Forschende"
WHEN = "Freitag, 13. November 2026, 9:00–12:45 Uhr"
WHERE = "Universität zu Lübeck, Ratzeburger Allee 160, Gebäude 64, PC-Pool (3. Etage)"
CONTACT = "[[TODO: Kontakt-E-Mail]]"
SL("surveyls_title", f"Anmeldung: {TITLE}")
SL("surveyls_description", "Anmeldung zum vierstündigen interaktiven Workshop.")
SL("surveyls_welcometext",
   f"<p>Vielen Dank für Ihr Interesse am Workshop <strong>{TITLE}</strong>.</p>"
   f"<p><strong>Termin:</strong> {WHEN}<br><strong>Ort:</strong> {WHERE}</p>"
   "<p>Es gibt maximal 12 Plätze, die in der Reihenfolge der Anmeldungen vergeben werden. Ist der Workshop "
   "ausgebucht, kommen Sie auf die Warteliste, und wir informieren Sie per E-Mail, sobald ein Platz frei wird.</p>"
   "<p>Die Anmeldung dauert etwa drei Minuten.</p>")
SL("surveyls_endtext",
   "<p><strong>Vielen Dank für Ihre Anmeldung!</strong></p>"
   "<p>Sie erhalten in Kürze eine Eingangsbestätigung an die angegebene E-Mail-Adresse. "
   "Vor dem Workshop melden wir uns mit der Teilnahmebestätigung und Hinweisen zur technischen Vorbereitung.</p>")
# Legal bases follow the IMIS "Datenschutzinformation für Veranstaltungsmanagement" (no consent), so the
# checkbox is an acknowledgement, not a consent.
SL("surveyls_policy_notice_label",
   "Ich habe die {STARTPOLICYLINK}Datenschutzhinweise{ENDPOLICYLINK} zur Kenntnis genommen.")
SL("surveyls_policy_error",
   "Bitte bestätigen Sie, dass Sie die Datenschutzhinweise zur Kenntnis genommen haben.")
SL("surveyls_policy_notice",
   "<h4>Datenschutzhinweise zur Workshop-Anmeldung</h4>"
   "<p><strong>Verantwortlich:</strong> Universität zu Lübeck, Ratzeburger Allee 160, 23562 Lübeck, vertreten durch "
   "das Institut für Menschzentrierte Interaktive Systeme (IMIS)<br>"
   f"<strong>Workshopleitung:</strong> Prof. Matthias König und Prof. André Calero Valdez, Universität zu Lübeck, {CONTACT}<br>"
   "<strong>Datenschutzbeauftragter:</strong> x-tention Informationstechnologie GmbH, datenschutz@uni-luebeck.de</p>"
   "<p><strong>Zweck:</strong> Wir verarbeiten Ihre Angaben, um den Workshop zu organisieren und vorzubereiten: "
   "Platzvergabe und Warteliste, Teilnahmebestätigung, Versand von Informationen zur technischen Vorbereitung sowie "
   "Abstimmung der Übungen auf die Gruppe.</p>"
   "<p><strong>Daten:</strong> Pflichtangaben sind Vor- und Nachname, E-Mail-Adresse, Einrichtung, Position, "
   "Betriebssystem, Erfahrung mit generativer KI und Zugang zu Claude. Freiwillig ist die Angabe einer Aufgabe aus "
   "Ihrem Forschungsalltag. Außerdem speichern wir den Zeitpunkt der Anmeldung. Ihre IP-Adresse wird nicht zusammen "
   "mit Ihren Angaben gespeichert.</p>"
   "<p><strong>Rechtsgrundlage:</strong> Für die Pflichtangaben Art. 6 Abs. 1 lit. b DSGVO (Anmeldung zur "
   "Veranstaltung) sowie Art. 6 Abs. 1 lit. e DSGVO in Verbindung mit § 3 Hochschulgesetz Schleswig-Holstein. Für die "
   "freiwillige Angabe unser berechtigtes Interesse, den Workshop auf die Gruppe abzustimmen (Art. 6 Abs. 1 lit. f "
   "DSGVO). Ohne die Pflichtangaben ist eine Anmeldung nicht möglich.</p>"
   "<p><strong>Empfänger und Speicherort:</strong> Die Daten werden auf dem LimeSurvey-Server des IMIS an der "
   "Universität zu Lübeck gespeichert, Name, E-Mail-Adresse und Freitext verschlüsselt. Die Anmeldungen bearbeitet "
   "die Workshopleitung. Eine Weitergabe an Dritte findet nicht statt.</p>"
   "<p><strong>Speicherdauer:</strong> Ihre Angaben werden nur so lange gespeichert, wie es für die Organisation des "
   "Workshops erforderlich ist, und spätestens drei Monate nach dem Workshop gelöscht.</p>"
   "<p><strong>Ihre Rechte:</strong> Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), "
   "Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch "
   "(Art. 21). Außerdem können Sie sich beim Unabhängigen Landeszentrum für Datenschutz Schleswig-Holstein (ULD) "
   "beschweren.</p>"
   "<p>Ausführliche Informationen finden Sie in der "
   "<a href='https://www.imis.uni-luebeck.de/datenschutz' target='_blank' rel='noopener'>Datenschutzerklärung des "
   "IMIS</a> und in der <a href='https://www.imis.uni-luebeck.de/datenschutz/datenschutzinformation-"
   "veranstaltungsmanagement' target='_blank' rel='noopener'>Datenschutzinformation für Veranstaltungsmanagement</a>.</p>")
# Sent to the participant via emailresponseto={EMAIL}; replaces the default text, which contains admin-only links.
SL("email_admin_responses_subj", f"Ihre Anmeldung: {TITLE}")
SL("email_admin_responses",
   "<p>Guten Tag,</p>"
   f"<p>vielen Dank für Ihre Anmeldung zum Workshop „{TITLE}“. Ihre Anmeldung ist bei uns eingegangen.</p>"
   f"<p><strong>Termin:</strong> {WHEN}<br><strong>Ort:</strong> {WHERE}</p>"
   "<p>Es gibt maximal 12 Plätze, die in der Reihenfolge der Anmeldungen vergeben werden. Vor dem Workshop melden "
   "wir uns mit Ihrer Teilnahmebestätigung oder Ihrem Platz auf der Warteliste sowie mit Hinweisen zur technischen "
   "Vorbereitung.</p>"
   "<p>Ihre Angaben:</p>{ANSWERTABLE}"
   f"<p>Möchten Sie Ihre Anmeldung zurückziehen, schreiben Sie bitte an {CONTACT}.</p>"
   "<p>Viele Grüße<br>Prof. Matthias König und Prof. André Calero Valdez</p>")

# --- Questions
G("Ihre Angaben")
Q("S", "VORNAME", "Vorname", encrypted="Y")
Q("S", "NACHNAME", "Nachname", encrypted="Y")
Q("S", "EMAIL", "E-Mail-Adresse",
  help="An diese Adresse senden wir die Bestätigung und alle weiteren Informationen zum Workshop.",
  encrypted="Y", validation=r"/^[^@\s]+@[^@\s]+\.[^@\s]+$/")
Q("S", "EINRICHTUNG", "Institut, Klinik oder Einrichtung")
Q("L", "POSITION", "Ihre aktuelle Position", other="Y")
A("PROM", "Promotion")
A("PDOC", "Postdoc")
A("PROF", "Professur oder Gruppenleitung")
A("WMA", "Wissenschaftliche Mitarbeit")

G("Vorbereitung", "Diese Angaben helfen uns, den Workshop auf die Gruppe abzustimmen.")
Q("L", "OS", "Mit welchem Betriebssystem arbeiten Sie auf Ihrem Laptop?",
  help="Wir bereiten die Installationshinweise passend zu Ihrem System vor.")
A("MAC", "macOS")
A("WIN", "Windows")
A("LIN", "Linux")
Q("L", "ERFAHRUNG", "Wie häufig nutzen Sie bisher generative KI (z. B. ChatGPT, Claude oder Copilot)?")
A("SELT", "Selten")
A("GELEG", "Gelegentlich, mehrmals im Monat")
A("REGEL", "Regelmäßig, mehrmals pro Woche")
A("TAEGL", "Täglich")
Q("L", "CLAUDE", "Haben Sie Zugang zu einer bezahlten Claude-Version?",
  help="Für die praktischen Übungen benötigen Sie eine bezahlte Claude-Version.")
A("JA", "Ja")
A("PLAN", "Noch nicht, ich richte sie bis zum Workshop ein")
A("UNKL", "Unklar, ich benötige dazu Informationen")
Q("T", "VORHABEN", "Gibt es eine Aufgabe aus Ihrem Forschungsalltag, die Sie gern mit agentischer KI angehen würden?",
  help="Optional. Bitte geben Sie keine vertraulichen oder personenbezogenen Daten an.",
  mandatory="N", encrypted="Y")

with open(OUT, "w", encoding="utf-8", newline="") as f:
    f.write("\t".join(COLS) + "\n")
    for r in rows:
        f.write("\t".join(r[c] for c in COLS) + "\n")
print(f"wrote {len(rows)} rows to {OUT}")

# Copy-paste version of the texts, for updating the already imported survey in the LimeSurvey UI.
sl = {r["name"]: r["text"] for r in rows if r["class"] == "SL"}
fields = [
    ("Privacy policy message", "Survey settings → Data policy settings → Privacy policy message", "surveyls_policy_notice"),
    ("Privacy policy checkbox label", "Survey settings → Data policy settings → Privacy policy checkbox label", "surveyls_policy_notice_label"),
    ("Privacy policy error message", "Survey settings → Data policy settings → Privacy policy error message", "surveyls_policy_error"),
    ("Confirmation email to participants", "Survey settings → Email templates → Detailed admin notification → Body (subject stays the same)", "email_admin_responses"),
    ("Welcome message", "Survey settings → Text elements → Welcome message", "surveyls_welcometext"),
]
with open(TEXTS, "w", encoding="utf-8") as f:
    f.write("# Survey texts for copy and paste\n\n"
            "Generated by `build_survey.py` together with `anmeldung.tsv`; edit the script, not this file.\n"
            "Paste each block into the field named above it. For the HTML fields, switch the editor to\n"
            "source mode first (the **Source** button in the editor toolbar), then replace everything in it.\n")
    if "[[TODO:" in "".join(sl[key] for _, _, key in fields):
        f.write("Replace the `[[TODO: …]]` placeholders before saving.\n")
    for title, where, key in fields:
        f.write(f"\n## {title}\n\n{where}\n\n```html\n{sl[key]}\n```\n")
print(f"wrote texts to {TEXTS}")
