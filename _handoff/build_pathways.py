"""Generate all pathway JSON files from CONTENT.md (one-time build script)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "content", "pathways")
os.makedirs(OUT, exist_ok=True)

# All dashes already swept; keep clean throughout.

def write(slug, data):
    with open(os.path.join(OUT, f"{slug}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"wrote {slug}.json")


# ============================================================================
# A1 - Community Legal Centres
# ============================================================================

CLC_BRISBANE = [
    {
        "slug": "atsils",
        "name": "ATSILS - Aboriginal and Torres Strait Islander Legal Service",
        "shortDescription": "Community-based legal service for Aboriginal and Torres Strait Islander peoples across Queensland.",
        "pathways": ["community-legal-centres", "first-nations-law"],
        "links": [],
        "contact": {
            "email": "careers@atsils.org.au",
            "phone": "(07) 3025 3888",
        },
        "body": "ATSILS is a community-based public benevolent organisation, established to provide professional and culturally competent legal services for Aboriginal and Torres Strait Islander peoples throughout Queensland. ATSILS provides legal services in criminal, family, child protection and civil law matters (which include human rights, anti-discrimination and coronial enquiries).\n\n**For Students:**\nATSILS welcomes Queensland students currently undertaking a Law/Justice/Indigenous Studies/Advocacy degree (or combination thereof) for placements in their Brisbane or regional offices. Whilst there are no fees for an internship with ATSILS, strong cultural competence training is provided. Apply via the Student Placement Program: https://www.atsils.org.au/student-placements/\n\n**For Graduates:**\nGraduate vacancies at https://www.atsils.org.au/job-vacancies/ and via Seek. Address selection criteria + provide employment skills/history. Three-member panel interview (in-person or Skype for Business). Prefers 2+ years post-admission, but less is welcome. Advocacy and court experience (Duty Lawyer + hearings) advantageous. Number of positions depends on yearly funding.",
    },
    {"slug": "ada-law", "name": "Aged and Disability Advocacy Law (ADA)", "pathways": ["community-legal-centres"], "links": []},
    {
        "slug": "basic-rights-queensland",
        "name": "Basic Rights Queensland",
        "shortDescription": "Free legal services in social security, Centrelink and disability discrimination law.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "contact": {"email": "brq@brq.org.au"},
        "body": "Basic Rights Queensland is a CLC providing free legal services in social security/Centrelink and disability discrimination law. They also provide community legal education and advocate for law reform.\n\n**For Students:**\nBasic Rights Qld runs two volunteer rosters per year - Jan to Jun (apps open November) and Jul to Dec (apps open May). Volunteers attend on a regular weekly basis under solicitor supervision. Available through LAWS5180 (Clinical Legal Education) at UQ. Direct email applications also accepted.",
    },
    {"slug": "bayside-community-legal-service", "name": "Bayside Community Legal Service", "pathways": ["community-legal-centres"], "links": []},
    {
        "slug": "caxton-legal-centre",
        "name": "Caxton Legal Centre",
        "shortDescription": "One of Queensland's longest-running CLCs - criminal law, social justice, family, civil, human rights and elder law.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "body": "Caxton Legal Centre is one of Queensland's longest-running CLCs, providing free legal advice and representation in criminal law, social justice law, family and civil law, human rights and elder law.\n\n**Three volunteer pathway types:**\n\n1. **Front Office Student Volunteers** - 4-hour weekly shift across the semester. Front-of-house, intake, and administrative support.\n2. **Clinical Legal Education** - LAWS5180 Consumer Law Clinic at UQ.\n3. **Volunteer Projects** - accessed via the UQ Pro Bono roster.",
    },
    {
        "slug": "edo",
        "name": "Environmental Defenders Office (EDO)",
        "shortDescription": "Public-interest environmental and planning law CLC.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "body": "EDO is a community legal centre specialising in public-interest environmental and planning law. They support communities advocating for environmental justice and law reform.\n\n**For Students:**\nStrong preference for students focused on environment, planning, or administrative law. Six-month application window. UQ students can access EDO via LAWS5180 Environmental Law Clinic.",
    },
    {
        "slug": "hub-community-legal",
        "name": "HUB Community Legal",
        "shortDescription": "Free legal advice and assistance across family, civil, criminal and consumer law.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "body": "HUB Community Legal provides free legal advice and assistance across a wide range of areas including family, civil, criminal, and consumer law.\n\n**For Students:**\nTwo annual application windows: January and July. Applications submitted via the HUB website.",
    },
    {"slug": "knowmore", "name": "Knowmore", "pathways": ["community-legal-centres"], "links": []},
    {
        "slug": "lawright",
        "name": "LawRight",
        "shortDescription": "Coordinates pro bono civil legal services for vulnerable people in Queensland.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "contact": {"email": "admin@lawright.org.au"},
        "body": "LawRight is a non-profit, community-based legal centre coordinating pro bono civil legal services for vulnerable people in Queensland.\n\n**Volunteer pathways:**\n\n- **Community & Health Justice Partnerships clinic** - embedded legal services in healthcare settings.\n- **Mater Health clinic** - partnership-based legal support.\n- **General volunteering** - apply via admin@lawright.org.au.",
    },
    {
        "slug": "lgbti-legal-service",
        "name": "LGBTI Legal Service",
        "shortDescription": "Free, confidential legal advice for LGBTIQ+ people in Queensland.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "contact": {"email": "mail@lgbtilegalservice.org"},
        "body": "The LGBTI Legal Service provides free, confidential legal advice and referrals for LGBTIQ+ people in Queensland. Practice areas include discrimination, family, criminal, and human rights law.",
    },
    {"slug": "northside-connect", "name": "Northside Connect", "pathways": ["community-legal-centres"], "links": []},
    {
        "slug": "prisoners-legal-service",
        "name": "Prisoners' Legal Service (PLS)",
        "shortDescription": "Free legal advice and representation for prisoners in Queensland.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "contact": {"email": "pls@plsqld.com"},
        "body": "PLS provides free legal advice and representation for prisoners in Queensland. Practice areas include parole, prison conditions, disciplinary breaches, and human rights.\n\n**Three student pathways:**\n\n- **UQ Prison Law Clinic** - LAWS5180.\n- **Mail Clinic** - written legal correspondence with prisoners.\n- **Community Call Back** - telephone-based legal advice.",
    },
    {
        "slug": "qai",
        "name": "Queensland Advocacy for Inclusion (QAI)",
        "shortDescription": "Independent advocacy and legal organisation for people with disability in Queensland.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "body": "QAI is an independent, community-based advocacy and legal organisation for people with disability in Queensland.\n\n**For Students:**\nVolunteer via UQ Pro Bono Centre placement OR independently. Ten-day commitment minimum. Apply 2 to 4 weeks before semester start or end of semester. Use the subject line \"Application to volunteer at QAI\" when applying directly.",
    },
    {
        "slug": "rails",
        "name": "Refugee and Immigration Legal Service (RAILS)",
        "shortDescription": "Free legal advice and representation to refugees, asylum seekers, and migrants.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "body": "RAILS provides free legal advice and representation to refugees, asylum seekers, and migrants in Queensland.\n\n**For Students:**\n\n- **UQ Refugee and Immigration Law Clinic** (LAWS5180).\n- **Day volunteer requirements:** 3rd year+, CV/cover letter/transcript. Three intakes per year (Feb / Jun-Jul / Nov). Commitment is 1 day/week for 3 months.",
    },
    {
        "slug": "sisters-inside",
        "name": "Sisters Inside Inc.",
        "shortDescription": "Independent advocacy for the human rights of women and girls in the criminal justice system.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "body": "Sisters Inside is an independent community organisation advocating for the human rights of women and girls in the criminal justice system.\n\n**Pathways:**\n\n- Apply via the Sisters Inside website.\n- Apply via UQ Pro Bono Centre.\n- **Dual-degree graduate pathways:** Children's Violence Prevention Worker, Youth Violence Prevention Worker, Policy Officer.",
    },
    {
        "slug": "tenants-queensland",
        "name": "Tenants Queensland",
        "shortDescription": "Queensland's specialist tenants' advice and advocacy service.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "contact": {"website": "https://tenantsqld.org.au/category/careers/", "email": "volunteer@tenantsqld.org.au"},
        "body": "Tenants Queensland is the state's specialist tenants' advice and advocacy service.\n\n**For Students:**\n\n- LAWS5180 access at UQ.\n- Volunteer applications via the careers page or volunteer email.",
    },
    {
        "slug": "wlsq",
        "name": "Women's Legal Service (WLSQ)",
        "shortDescription": "Free legal services for women across Queensland: family law, domestic violence, discrimination.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "contact": {"email": "volunteers@wlsq.org.au"},
        "body": "WLSQ provides free legal services to women across Queensland, with a particular focus on family law, domestic violence, and discrimination.\n\n**Important:** WLSQ is a women's-only space. Client-facing roles are reserved for female-identifying staff and volunteers.",
    },
    {
        "slug": "yfs-legal",
        "name": "YFS Legal",
        "shortDescription": "Community-based legal service operating in Logan and surrounding region.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "body": "YFS Legal is a community-based legal service operating in Logan and the surrounding region.\n\n**Two clinic pathways at UQ:**\n\n- **Generalist Legal Task Clinic** (UQ Pro Bono).\n- **Culturally Safe criminal law practice clinic** (LAWS5180).",
    },
    {
        "slug": "youth-advocacy-centre",
        "name": "Youth Advocacy Centre",
        "shortDescription": "Free legal and social work services for young people aged 10 to 18 in Queensland.",
        "pathways": ["community-legal-centres"],
        "links": [],
        "contact": {"email": "admin@yac.net.au"},
        "body": "The Youth Advocacy Centre (YAC) provides free legal and social work services for young people aged 10 to 18 in Queensland.\n\n**Application:** cover letter + resume to admin@yac.net.au.",
    },
]

CLC_REGIONAL_NAMES = [
    "Aboriginal & Torres Strait Islander Women's Legal Services North Queensland",
    "Aboriginal Family Legal Services Queensland (Maruma-li-mari)",
    "Cairns Community Legal Centre",
    "Central Queensland Community Legal Centre (Rockhampton)",
    "Gold Coast Community Legal Centre & Advice Bureau",
    "Institute for Urban Indigenous Health (Legal Service)",
    "Junkuri Laka Community Legal Centre Aboriginal Corporation (Mornington Island)",
    "Pine Rivers Community Legal Service",
    "Mackay Regional Community Legal Centre",
    "My Community Legal Gold Coast",
    "Queensland Indigenous Family Violence Legal Service",
    "Suncoast Community Legal Service",
    "TASC Community Legal Centre (Toowoomba)",
    "Townsville Community Legal Service",
    "Wide Bay Burnett Community Legal Service",
]

def slugify(name):
    import re
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

CLC_REGIONAL = [
    {"slug": slugify(n), "name": n, "pathways": ["community-legal-centres"], "links": []}
    for n in CLC_REGIONAL_NAMES
]

write("community-legal-centres", {
    "slug": "community-legal-centres",
    "name": "Community Legal Centres",
    "iconName": "users-round",
    "status": "published",
    "introAbove": "Community legal centres (CLCs) are independent, community organisations providing equitable and accessible legal services. CLCs tend to service specific demographics or a particular area of law, such as family law, employment law, criminal law and environmental law. Services provided generally include free legal advice, referrals, representation, community legal education, and advocating for law reform.\n\nA range of different volunteering opportunities are available in CLCs across Brisbane and the wider Queensland area. The UQ Pro Bono Centre is an excellent starting point to engage with CLCs and offers a wide range of opportunities for students to participate in the delivery of pro bono legal services in Queensland. The Centre oversees the Law School's Clinical Legal Education Program, research support for pro bono activities, the Pro Bono roster and the Barrister's Assistance Team.\n\n**Reference links:**\n- [Community Legal Centres Queensland](http://communitylegalqld.org.au/)\n- [Community Legal Centres Australia](https://clcs.org.au/)",
    "sections": [
        {
            "heading": "Brisbane-Based",
            "displayMode": "cards",
            "orgs": CLC_BRISBANE,
            "showTestimonialsButton": False,
        },
        {
            "heading": "Other Queensland",
            "displayMode": "cards",
            "orgs": CLC_REGIONAL,
            "showTestimonialsButton": False,
        },
    ],
})


# ============================================================================
# A2 - Legal Aid Queensland
# ============================================================================

write("legal-aid-queensland", {
    "slug": "legal-aid-queensland",
    "name": "Legal Aid Queensland",
    "iconName": "scale",
    "status": "published",
    "topLevelLinks": [
        {
            "label": "About Legal Aid Queensland",
            "type": "modal",
            "modalContent": "Legal Aid Queensland (LAQ) is a statutory authority established under the *Legal Aid Queensland Act 1997* providing legal assistance to financially disadvantaged people across Queensland. With over 600 staff and 14 offices, LAQ covers criminal, family, civil, discrimination, sexual harassment, employment, credit/debt, Mental Health Court, and domestic and family violence work. Duty lawyers operate in the Magistrates Court, Federal Circuit and Family Court, and Children's Court.",
        },
        {
            "label": "Current Vacancies",
            "type": "external",
            "href": "https://www.legalaid.qld.gov.au/About-us/Work-for-us",
        },
        {"label": "Testimonials", "type": "testimonials-modal"},
    ],
    "sections": [],
    "bodyContent": "## For Students\n\nLAQ has a Strategic Workforce Plan and a First Nations Strategy that guide its hiring. Graduate opportunities are advertised on SmartJobs and via the Work for Us portal. For first- and second-year students, LAQ regularly advertises Litigation Support Officer and Client Information Officer roles on SmartJobs.\n\nContact: BEL Student Employability Team. Follow LAQ on LinkedIn, Facebook, and Instagram for current openings.",
    "relatedPathways": ["criminal-law", "family-law"],
})


# ============================================================================
# A3 - Associateships
# ============================================================================

QLD_ASSOC = [
    {"slug": "supreme-district", "name": "Supreme and District Court", "modal": "Applications open in December, approximately 14 months before commencement. Apply directly to an individual judge OR via a general pool. https://courts.qld.gov.au/about/jobs-with-the-courts/judges-associates"},
    {"slug": "land-court", "name": "Land Court", "modal": "Application Form + Questionnaire + cover letter (1 page max) + CV (5 pages max with 2 referees) + transcript. Submit to the Executive Assistant. https://courts.qld.gov.au/courts/land-court/land-court-associates"},
    {"slug": "qcat", "name": "QCAT", "modal": "Applications open and close in August. Required: Application Form + Cover letter + CV + transcript. Submit to qcattribunal.appointments@justice.qld.gov.au."},
    {"slug": "qirc", "name": "QIRC", "modal": "Vacancies advertised on SmartJobs and Seek. https://www.qirc.qld.gov.au/"},
]

CW_ASSOC = [
    {"slug": "federal-court", "name": "Federal Court of Australia", "modal": "Apply to an individual judge. Associateships are appointed 1 to 2 years in advance, typically in January or February. query@fedcourt.gov.au · https://www.fedcourt.gov.au/about/employment/associates"},
    {"slug": "fccfc", "name": "Federal Circuit and Family Court of Australia", "modal": "Recruitment via the Court's online recruitment system. Vacancies advertised on APSJobs (https://www.apsjobs.gov.au/)."},
    {"slug": "art", "name": "Administrative Review Tribunal", "modal": "Recruitment via the ART Career Opportunities portal. recruitment@art.gov.au · (02) 9276 5443 · https://www.art.gov.au/about-us/careers"},
    {"slug": "fwc", "name": "Fair Work Commission", "modal": "Own job portal. Associates support approximately 55 Members. Roles advertised at APS5 level for 12 to 18 months (extendable to 2 years). Merit pool valid for 18 months from date of advertisement."},
    {"slug": "nntt", "name": "National Native Title Tribunal", "modal": "https://www.nntt.gov.au/aboutus/careers and https://www.fedcourt.gov.au/about/employment"},
]

def assoc_org(slug, name, modal):
    return {
        "slug": slug,
        "name": name,
        "pathways": ["associateships"],
        "links": [{"label": name, "type": "modal", "modalContent": modal}],
    }

write("associateships", {
    "slug": "associateships",
    "name": "Associateships",
    "iconName": "gavel",
    "status": "published",
    "sections": [
        {
            "heading": "Queensland Jurisdiction",
            "displayMode": "buttonRow",
            "orgs": [assoc_org(o["slug"], o["name"], o["modal"]) for o in QLD_ASSOC],
            "testimonialsScope": "QLD Jurisdiction",
        },
        {
            "heading": "Commonwealth Jurisdiction",
            "displayMode": "buttonRow",
            "orgs": [assoc_org(o["slug"], o["name"], o["modal"]) for o in CW_ASSOC],
            "testimonialsScope": "Commonwealth Jurisdiction",
        },
    ],
    "bodyContent": "## What is an Associate?\n\nA Judge's Associate assists a judge or court. In Australia, an Associate is typically a recent graduate or a lawyer assisting a specific judge. The role also extends to Tribunal Members at the Administrative Appeals Tribunal (AAT), QCAT, and the Fair Work Commission.\n\n## What does Associateship involve?\n\nAssociateship is the privilege of working with experienced judges as mentors. The role involves frequent attendance at court, observation of oral advocacy, and exposure to judicial decision-making.\n\nDaily tasks include: assisting in court, summarising matters, proofreading judgments, liaising with parties, and conducting legal research. The role often includes circuit travel and extra-judicial tasks such as function planning and speechwriting.\n\nCareer benefits flow into innumerable fields - many alumni cite it as the single most formative year of their early career.\n\n## How to Apply?\n\nApplication processes vary per Court and Tribunal. Generally, you'll need a CV, a cover letter, and an academic transcript. An interview with the judge or member is typical for shortlisted candidates.",
})


# ============================================================================
# A4 - Government & Public Service
# ============================================================================

FED_GOV = [
    ("ag-dept", "Attorney General's Department", "Responsibilities span rule of law, national security, emergency management, families and marriage, rights, legal systems, crime and corruption, and international relations. The Australian Government Solicitor (AGS) provides legal services to the Commonwealth.\n\n12-month graduate program (policy or legal practice stream). Applications open in March. https://www.ag.gov.au/about-us/careers/employment-programs · HR.Assist@ag.gov.au"),
    ("accc", "ACCC", "Enforces the *Competition and Consumer Act 2010*; promotes competition; consumer protection; regulates monopoly infrastructure.\n\nGraduate program. Applications open in March each year for the following February start. https://www.accc.gov.au/about-us/careers/graduate-opportunities · grad.jobs@accc.gov.au"),
    ("asic", "ASIC", "Australian corporate, markets, and financial services regulator.\n\n12-month graduate program with 4 x 4-month rotations across surveillance, investigations, intelligence, data analytics, and consumer research. Applications open in June. Recruitment includes video interview + psychometric testing. https://careers.asic.gov.au/Graduate-program.html · graduateprogram@asic.gov.au"),
    ("ato", "Australian Taxation Office", "Lawyer / Prosecution Officer / Litigator pathways, plus a paid university internship.\n\n[ATO careers - lawyers](https://www.ato.gov.au/about-ato/careers/specialist-careers/lawyers-prosecutors-and-litigators) · [University Partnership Employment Program](https://www.ato.gov.au/careers/graduate-and-entry-level-programs/university-partnership-employment-program)"),
    ("dfat", "Department of Foreign Affairs & Trade", "2-year graduate program (policy or corporate management streams). Applications open in February. Submission requires: 500-word response + 100-word outline + 2 referees + achievements + extracurriculars + work experience. https://www.dfat.gov.au/careers/dfat-aps-careers/graduate-program · gradrec@dfat.gov.au"),
    ("pmc", "Department of the Prime Minister & the Cabinet", "12-month graduate program based in Canberra with regional rotations. Streams: generalist, Indigenous Affairs, or Corporate and Government. Applications close end of April. https://www.pmc.gov.au/join-us/entry-level-programs/graduate-program · EntryLevelPrograms@pmc.gov.au"),
    ("treasury-fed", "Treasury (Federal)", "Provides advice, analysis, and legislation across macro to microeconomic policy - fiscal, foreign investment, tax, financial services, social, and international economic.\n\n2-year Canberra-based graduate program with 2 x 1-year rotations. Applications open in March. https://graduates.treasury.gov.au/ · graduateprogram@treasury.gov.au"),
]

QLD_GOV = [
    ("lsc-qld", "Legal Services Commission (Qld)", "Independent government body regulating the legal profession in Queensland. Investigates complaints. Together with the Bar Association of Queensland and Queensland Law Society, the LSC is the sole authority empowered to prosecute legal practitioners. lsc@lsc.qld.gov.au"),
    ("future-leaders", "Future Leaders Graduate Program", "Queensland Government's flagship 2-year program. Sector-wide rotations. Applications open in March and close in April of the year prior. https://www.qld.gov.au/jobs/graduates/graduate-programs/programs/future-leaders-graduate-program\n\n*(Note: an earlier version of the source called this \"Policy Futures Graduate Program\" - Future Leaders is the current canonical name.)*"),
    ("qld-doj", "Queensland Department of Justice", "Flagship Law and Justice Graduate Program - 2-year program, open to Law / Criminology / Social Work / Policy / Psychology / related degrees. Focus areas: justice reform, community safety, fair services. https://www.qld.gov.au/jobs/graduates/graduate-programs/programs/law-justice"),
    ("qld-treasury", "Queensland Treasury", "State finances and economy expert. Variety of project-based roles. https://www.qld.gov.au/jobs/graduates/graduate-programs/programs/treasury-gradstart · gradprog@treasury.qld.gov.au"),
]

write("government-and-public-service", {
    "slug": "government-and-public-service",
    "name": "Government & Public Service",
    "iconName": "landmark",
    "status": "published",
    "introAbove": "Whether you work within a department or statutory body, your role would ultimately involve promoting and safeguarding the interests of the wider Queensland or Australian community.\n\nWorking within the public service or government sector offers numerous advantages: there is enormous variety in the roles available, and just being in a diverse environment opens your eyes to career options you might never have considered; secondments create lots of opportunities to develop your skills and there is astonishing mobility within the sector; and greater opportunities for work-life balance (flex time, compressed hours, part-time work, 48/52 or recreation leave at half pay, etc.). Although still subject to operational convenience, they are better than you could negotiate in most private firms.\n\nLegal skills are valuable in the public sector, in legal, policy and program roles. While both the Queensland and federal public sectors offer graduate programs, there are still several ways of 'getting a foot in the door'. If you accept an entry level role, there are frequent opportunities for advancement within and across departments.",
    "sections": [
        {
            "heading": "Federal",
            "displayMode": "buttonRow",
            "orgs": [assoc_org(s, n, m) for s, n, m in FED_GOV],
            "testimonialsScope": "Federal Government",
        },
        {
            "heading": "Queensland",
            "displayMode": "buttonRow",
            "orgs": [assoc_org(s, n, m) for s, n, m in QLD_GOV],
            "testimonialsScope": "Queensland Government",
        },
    ],
    "relatedPathways": ["criminal-law", "international-law"],
})


# ============================================================================
# A5 - First Nations' Law
# ============================================================================

write("first-nations-law", {
    "slug": "first-nations-law",
    "name": "First Nations' Law",
    "iconName": "leaf",
    "status": "published",
    "introAbove": "The following workplaces provide law students and graduates with excellent opportunities to assist Australia's First Nations people:",
    "topLevelLinks": [{"label": "Testimonials", "type": "testimonials-modal"}],
    "sections": [
        {
            "displayMode": "table",
            "orgs": [
                {
                    "slug": "aurora-project",
                    "name": "The Aurora Project",
                    "pathways": ["first-nations-law"],
                    "links": [],
                    "body": "The Aurora Education Foundation internship program welcomes Indigenous and non-Indigenous students from law, social science, and health. Native title, land rights, policy, research, and social justice. Host organisations include Native Title Representative Bodies and Prescribed Body Corporates Australia-wide.\n\n4 to 6 weeks unpaid full-time (part-time negotiable). Alumni network; sometimes leads to paid employment.\n\n**For Students:** Winter intake applications open in March; Summer intake in August. For law applicants: enrolled in or completed Property Law (incl. native title) - partial completion may still be eligible. Required: resume + transcript + 2 written references (1 professional, 1 academic) + cover letter (cultural awareness emphasis).\n\nScholarships for Indigenous interns cover daily living + travel + accommodation. https://aurorafoundation.com.au/our-work/internship-program/",
                },
                {
                    "slug": "qsnts",
                    "name": "Queensland South Native Title Service (QSNTS)",
                    "pathways": ["first-nations-law"],
                    "links": [],
                    "body": "Native Title Service Provider - government-funded delivery of legal advice to Traditional Owners on Native Title. Endeavours to secure self-determination, rights-based recognition, and fair agreements and compensation for First Nations People.\n\nInternships via Aurora and case-by-case applications. Position listings: https://qsnts.com.au/",
                },
                {
                    "slug": "atsils",
                    "name": "Aboriginal and Torres Strait Islander Legal Service (ATSILS)",
                    "pathways": ["first-nations-law", "community-legal-centres"],
                    "links": [],
                    "body": "*(Cross-referenced with [Community Legal Centres](/pathways/community-legal-centres/).)*\n\nATSILS welcomes Queensland students studying Law, Justice, Indigenous Studies, Advocacy, or a combination. Student Placement Program in Brisbane or regional offices: criminal, family, child protection, civil (incl. human rights, coronial enquiries). https://www.atsils.org.au/student-placements/\n\nNo internship fees, but strong cultural competence training is provided.\n\n**For graduates:** https://www.atsils.org.au/job-vacancies/ + Seek. Address selection criteria + employment skills/history. Three-member panel interview (in-person or Skype for Business). Prefers 2+ years post-admission, but less is welcome. Advocacy and court experience (Duty Lawyer + hearings) advantageous. Number of positions depends on yearly funding.",
                },
            ],
            "showTestimonialsButton": False,
        }
    ],
    "relatedPathways": ["community-legal-centres"],
})


# ============================================================================
# A6 - International Law
# ============================================================================

INTL_ORGS = [
    ("office-of-international-law", "Office of International Law", "Within the Commonwealth Attorney-General's Department. *(Cross-link to [Government & Public Service](/pathways/government-and-public-service/).)*"),
    ("un-ypp", "United Nations - Young Professionals Programme (YPP)", "Recruitment for international civil servants with the UN Secretariat. Entrance examination + structured professional development. P-1 / P-2 entry levels. P-2 requires a bachelor's + 2 years experience OR a master's. Applicants must be 32 years old or younger and a national of a participating UN Member State. Applications open in October via the Inspira portal. https://careers.un.org/young-professionals-programme"),
    ("un-volunteer", "United Nations - Volunteer Programme (UNV)", "Managed by UNDP, supporting the SDGs. International / national / online volunteering. Age 18+. 6 to 12 months, renewable up to 4 years. No salary, but Volunteer Living Allowance + travel + health insurance + resettlement allowance. Apply via the UNV Unified Volunteering Platform. https://www.unv.org/become-volunteer"),
    ("icj-internship", "International Court of Justice - Internship Programme", "Open to students and young professionals. Tasks under Registry officials' supervision; placements across Registry departments and divisions. Limited number per year. Unpaid (own travel, accommodation, medical insurance). English or French required. Apply via the ICJ eRecruitment System only - no hardcopy or email. https://www.icj-cij.org/internships"),
    ("icc-internship", "International Criminal Court - Internship Programme", "For final-year university students OR graduates with under 3 years relevant full-time experience. 3 to 6 months full-time at The Hague. Unpaid; own living expenses. English or French. https://www.icc-cpi.int/jobs/internships-and-visiting-professionals"),
    ("icc-vpp", "International Criminal Court - Visiting Professionals Programme", "Bachelor's + 3 years relevant full-time experience. 1 to 6 months full-time. Generally unpaid, but limited funded positions via the ICC Trust Fund for candidates from developing countries. Same URL as above."),
    ("pca-internship", "Permanent Court of Arbitration - Internship Programme", "3 months starting in January / April / July / October. Apply 4 months in advance. Final-year law students or recent graduates with strong academics. Australian native English satisfies the language requirement; Arabic, Chinese, Russian, or Spanish advantageous. Self-funded - applicants need adequate financial resources + health insurance for relocating to Vienna or Mauritius. The PCA provides supporting documentation if a travel visa is required. https://pca-cpa.org/en/about/employment/internship-program/"),
    ("uq-embassy", "UQ Embassy Internship Program", "Strengthens UQ-embassy ties through research, reports, and events. All unpaid. Eligibility: Australian citizen or PR + returning to full-time study + faculty approval (academic credit OR unpaid extracurricular). UQ Law / Political Science students can enrol POLS3801 or POLS7521 for credit. Runs over summer and winter breaks, Canberra-based. https://employability.uq.edu.au/uq-embassy-internship-program"),
]

write("international-law", {
    "slug": "international-law",
    "name": "International Law",
    "iconName": "globe",
    "status": "published",
    "introAbove": "The international law field offers a diverse range of careers domestically and beyond Australia. With human rights breaches and cross-national conflicts at the cornerstone of the public international law sector, there is a major intersection between public policy and international law. Public international law encompasses diverse practice areas and practices in a vast range of organisations.",
    "topLevelLinks": [{"label": "Testimonials", "type": "testimonials-modal"}],
    "sections": [
        {
            "displayMode": "table",
            "orgs": [
                {"slug": s, "name": n, "pathways": ["international-law"], "links": [], "body": b}
                for s, n, b in INTL_ORGS
            ],
            "showTestimonialsButton": False,
        }
    ],
    "relatedPathways": ["government-and-public-service", "criminal-law"],
})


# ============================================================================
# A7 - Family Law
# ============================================================================

write("family-law", {
    "slug": "family-law",
    "name": "Family Law",
    "iconName": "heart-handshake",
    "status": "published",
    "introBelow": "Family law is one of the more challenging specialities of law because it involves counselling people through difficult periods of their lives. As a family lawyer, you will assist your clients in navigating divorces, property settlements, post-separation parenting arrangements, financial agreements (\"prenups\"), child support disputes and agreements. Family lawyers may also deal with family matters involving State based issues such as adoption applications and surrogacy arrangements. Family law can also encompass many different areas of law, such as property law, criminal law and even private international law. While some lawyers specialise in one of these processes, many instead maintain a 'general practice', advising their clients on a range of issues.",
    "sections": [
        {
            "displayMode": "buttonRow",
            "orgs": [
                {
                    "slug": "family-law-organisations",
                    "name": "Organisations",
                    "pathways": ["family-law"],
                    "links": [
                        {
                            "label": "Organisations",
                            "type": "modal",
                            "modalContent": "## Brisbane Family Law Centre\n\nBrisbane Family Law Centre, led by Director Clarissa Rayward, was established in 2008. The firm prides themselves on providing quality legal advice, a very high standard of client care, as well as a genuine and sincere service. Brisbane Family Law Centre is a specialist family law firm that provides a range of services across family and relationship law, including on matters relating to divorce, surrogacy, adoption, spousal maintenance and property settlement. Career opportunities with the firm can be found on their website. The firm in the past has run work experience programs for students.\n\n## Firms Practicing Family Law\n\n- Barry Nilsson\n- HopgoodGanim\n- Phillips Family Law\n- Damien Greer Lawyers\n- Hirst & Co\n- Mills Oakley\n- Naughton McCarthy\n- Ryan Kruger\n- Cooper Grace Ward\n- DA Family Lawyers\n- Hartley Healy\n- Simonidis Steel\n- Bell Dore\n- Daykin Family Law\n- Feeney Family Law\n- Michael Lynch\n- Page Provan\n- Parry Coates\n- Stewart",
                        }
                    ],
                }
            ],
        }
    ],
    "relatedPathways": ["legal-aid-queensland", "community-legal-centres"],
})


# ============================================================================
# A8 - Criminal Law
# ============================================================================

CRIMINAL_GOV = "**The Office of the Commonwealth Director of Public Prosecutions (CDPP)**\n\nThe Office of the Commonwealth Director of Public Prosecutions (CDPP) is an independent prosecution service established by Commonwealth Parliament to prosecute alleged offences against Commonwealth law. The CDPP plays a critical role in our criminal justice system by prosecuting crimes against Commonwealth laws, from online child exploitation through to counter-terrorism and war crimes.\n\nInfo: https://www.cdpp.gov.au/careers · Phone: 02 6206 5666 · Email: recruitment@cdpp.gov.au\n\n**The Office of the Director of Public Prosecutions (ODPP)**\n\nThe Office of the Director of Public Prosecutions prosecutes criminal matters for the state of Queensland. If you're interested in working as a criminal barrister or in the criminal field generally, the ODPP offers a Work Experience Placement Program (WEPP) throughout the year and in a number of locations across Queensland. Applications should be made directly to the TC Beirne School of Law.\n\nInfo: https://law.uq.edu.au/current-students/careersoverseas/work/odpp"

CRIMINAL_PRIV = "**Criminal Defence (intro)**\n\nIf you have an interest in criminal defence and wish to gain experience in the area, reach out to criminal defence firms and request work experience or job opportunities as a clerk. Some firms offer a Summer Clerkship Program, but these opportunities are rare. Such roles often involve appearing in court for mentions, allowing you to interact with the courts at an early stage in your law career. Making contacts in this manner is important for criminal defence, and firms are ordinarily open to taking on work experience and PLT students. Many criminal defence firms also provide services in relation to employment law, traffic law and domestic violence. Further, closely linked to criminal law matters is human rights law, and with the *Human Rights Act 2019* (Qld), the intersection between these areas is an interesting space to watch.\n\n**Firms include:**\n\n**Gilshenan & Luton Lawyers**\n\nTop-tier criminal law firm that commenced in 1924. They defend criminal charges across the entire range of offences - from straightforward matters such as minor assaults and drug possession to the most complex cases of homicide, financial crime and large-scale drug matters.\n\n**Fisher Dore Lawyers**\n\nLeading criminal law firm in Queensland with offices in Brisbane, Beenleigh, Rockhampton, Bundaberg, Mackay and Maroochydore. With 45 combined years of experience between their two accredited criminal law specialists and 154 appeals in 13 years, they are recognised as first tier in the *Doyle's Guide*. They represent clients in a wide range of criminal law matters, including drug charges, cyber and computer crime, professional misconduct, human rights and migration.\n\n**Robertson O'Gorman Solicitors**\n\nLeading criminal law firm in Queensland recognised consistently as first-tier by the *Doyle's Guide*. They specialise in criminal law but have significant experience in other fields, including employment law and traffic law. With more than 40 years of experience, they have represented clients in the High Court of Australia on numerous occasions."

write("criminal-law", {
    "slug": "criminal-law",
    "name": "Criminal Law",
    "iconName": "shield",
    "status": "published",
    "topLevelLinks": [{"label": "Testimonials", "type": "testimonials-modal"}],
    "introAbove": "Criminal law sits at the heart of justice - it's where law meets human lives at their most vulnerable and consequential. For law students drawn to purposeful, people-centred work, few areas of practice are more directly meaningful.\n\nCareer paths in criminal law reflect a spectrum of values. If you're motivated by advocacy and access to justice, working as a defence lawyer - in private practice or through Legal Aid Queensland - means ensuring every person, regardless of background, receives fair representation. If fairness means accountability, a career as a prosecutor with the Office of the Director of Public Prosecutions (DPP) puts you at the front line of upholding community standards. Those driven by systemic change may find their place in policy roles within the Queensland Department of Justice, or in reform-focused organisations like the Queensland Law Reform Commission.\n\nFor students with a global outlook, international criminal law - practised through institutions like the ICC or UN tribunals - offers the opportunity to address the gravest crimes on the world stage.",
    "sections": [
        {
            "heading": "Areas of Practising Criminal Law",
            "displayMode": "buttonRow",
            "orgs": [
                {"slug": "government", "name": "Government", "pathways": ["criminal-law"], "links": [{"label": "Government", "type": "modal", "modalContent": CRIMINAL_GOV}]},
                {"slug": "private-practice", "name": "Private Practice", "pathways": ["criminal-law"], "links": [{"label": "Private Practice", "type": "modal", "modalContent": CRIMINAL_PRIV}]},
            ],
            "showTestimonialsButton": False,
        }
    ],
    "relatedPathways": ["legal-aid-queensland", "government-and-public-service", "international-law"],
})


# ============================================================================
# A9 - Plaintiff Personal Injury
# ============================================================================

PPI_MODAL = "## Maurice Blackburn Lawyers\n\nFounded 1919 by Maurice McRae Blackburn (Labor Party politician and social justice activist). An Australian plaintiff law firm that has represented clients in a number of high-profile cases, including the Centro Class Action and the MUA Waterfront Dispute Case.\n\nThe 12-month Graduate Program provides a broad range of training designed to give you insight into all aspects of plaintiff law. The firm also supports its graduates in their completion of Practical Legal Training. Graduate programs are only run in Queensland and Victoria. Previous Seasonal Clerks and current employees are eligible to apply for a priority offer to commence as a Law Graduate. The firm runs its seasonal clerkship program annually, with applications opening in the first week of March.\n\n## CZ Legal\n\nBoutique Brisbane-based law firm specialising in plaintiff personal injury. The lawyers have many years of experience running matters in Queensland and Federal jurisdictions.\n\nCZ Legal takes a practical, personal, and compassionate approach. The lawyers understand the client as a person and assist them on a 'no win, no fee' basis. The team provides multilingual legal services that assist the diverse communities in Brisbane. The team works tirelessly to achieve the best possible outcome for their client. As licensed members of the Queensland Law Society, CZ Legal serves the public with fairness and professionalism.\n\nSee more here: https://www.czinjurylaw.com/contact-us\n\n## Shine Lawyers\n\nFounded more than 40 years ago in Toowoomba, by a lawyer who wanted to do things differently and believed in always putting his clients first. They're a firm specialising in personal injury compensation law, operating on a no win no fee basis. The firm has expanded into providing professional negligence, coal seam gas, and aviation law legal services through a number of acquisitions. However, they are primarily renowned for being a leading firm in motor vehicle accident compensation and work injury compensation. Shine Lawyers also has many offices in regional and rural Australia. For those interested in undertaking personal injury work in a rural area, Shine Lawyers may be the firm for you.\n\nSee more about careers here: https://www.shine.com.au/careers"

write("plaintiff-personal-injury", {
    "slug": "plaintiff-personal-injury",
    "name": "Plaintiff Personal Injury",
    "iconName": "stethoscope",
    "status": "published",
    "introBelow": "Personal injury law deals with general physical and/or psychological damages to an individual that are the fault of another responsible party. Plaintiff personal injury lawyers work to ensure that their clients' rights are protected, and that the client receives a fair settlement to compensate for his or her injuries. A career in plaintiff personal injury law is perfect for an individual with a strong sense of social justice, and who would enjoy a career with a high degree of client contact.",
    "sections": [
        {
            "displayMode": "buttonRow",
            "orgs": [{"slug": "ppi-orgs", "name": "Organisations", "pathways": ["plaintiff-personal-injury"], "links": [{"label": "Organisations", "type": "modal", "modalContent": PPI_MODAL}]}],
        }
    ],
})


# ============================================================================
# A10 - Boutique & Other Specialties
# ============================================================================

BOUTIQUE_MODAL = "Some Brisbane boutique firms include:\n\n## Kindra Migration Lawyers\n\nAward-winning Australian immigration law firm, formerly known as WLW Migration Lawyers, which rebranded in November 2025. Founded in 2015 by Jessica Williamson, James Wardlaw, and Simon Leske, the firm has grown from a small practice into a national team with offices in Melbourne and Brisbane, covering skilled migration, employer-sponsored visas, partner and family visas, business visas, citizenship, and appeals. Their Bridge Project also provides pro bono migration assistance to those who cannot afford full representation.\n\nSee more about careers here: https://kindramigration.com.au/careers/\n\n## Griffith Hack Lawyers\n\nSpecialist intellectual property firm. The firm aims to provide a range of intellectual property services including analysing the existing IP landscape to inform strategic and innovation investment decisions, assisting clients to obtain the maximum research and development funding available as well as guiding the integration of IP strategy with business strategy.\n\nSee more careers information here: https://www.griffithhack.com/about-us/careers/\n\n## Leanne Bowie Lawyers\n\nBoutique Australian firm specialising in environmental, planning, and resumption law. The team at Leanne Bowie are experienced in complex resource-based projects, infrastructure projects, and a range of other development projects. Leanne Bowie Lawyers also provides policy and legislative advice.\n\nSee more careers information here: https://www.bowielaw.com.au/careers\n\n## Samuta McComber Lawyers\n\nMicro-firm that practices exclusively in migration law, specifically complex migration matters (including visa cancellations under section 501 and section 116 of the *Migration Act 1958*). It also assists with visa applications. Samuta McComber Lawyers regularly appears at the Administrative Appeals Tribunal (AAT) as advocates for applicants.\n\nSee more: https://samutamccomber.com.au/contact-us"

write("boutique-and-other-specialties", {
    "slug": "boutique-and-other-specialties",
    "name": "Boutique & Other Specialties",
    "iconName": "gem",
    "status": "published",
    "introBelow": "The first point to remember about boutique firms is that the term \"boutique\" is not simply a euphemism for small. Rather, boutique law firms specialise in a niche area of law. Therefore, a boutique firm isn't about size; it's about specialisation. A boutique law firm can provide expert legal advice and services to individuals or businesses in one or a select few areas of the law. Although midsize and large law firms have structured themselves to offer a broad range of services, a growing number of lawyers are setting up these smaller practices, choosing to focus the work of the entire firm on one area of law.\n\nIt is important to note that boutique law firms generally do not have an official graduate program and offer legal positions within the firm on an intermittent basis. These positions will often be advertised on job search websites, university job boards and on the firm's website.",
    "sections": [
        {
            "displayMode": "buttonRow",
            "orgs": [{"slug": "boutique-orgs", "name": "Organisations", "pathways": ["boutique-and-other-specialties"], "links": [{"label": "Organisations", "type": "modal", "modalContent": BOUTIQUE_MODAL}]}],
        }
    ],
})


# ============================================================================
# A11 - Academia
# ============================================================================

write("academia", {
    "slug": "academia",
    "name": "Academia",
    "iconName": "book-open",
    "status": "published",
    "topLevelLinks": [{"label": "Testimonials", "type": "testimonials-modal"}],
    "sections": [],
    "bodyContent": "## Is Academia for you?\n\nThe role of an academic in a university context generally has three component parts: research, teaching, and service. Research entails publishing work both as an individual and in collaboration with other academics. Being able to work in a group is therefore a key skill for those considering a career in academia. Teaching involves taking university courses, both as a lecturer and a tutor, and may involve acting as a supervisor for students in research higher degree and PhD programs. Service encompasses a broad range of things from coordinating extra-curricular programs, to facilitating university community outreach initiatives.\n\nAcademia is an attractive career for those with an inquiring mind and a passion for research. If you choose to pursue a career as an academic, you will have the unique opportunity to become an expert in an area of the law and directly contribute to the development of a field of legal knowledge. As respected experts in their chosen field, academics have influence on the interpretation and development of the law through their writing. There are also international opportunities available for those interested in academia. Academics may travel to other countries for conferences or to carry out research and may be appointed to positions in overseas universities.\n\n## Pathways to Academia\n\nSecuring a position at a university faculty is no mean feat: such positions are often highly competitive. For those interested in a career as an academic there are certain things to be aware of to give you the best chance of landing a job as an academic. First, it is increasingly important to have completed post-graduate research in an allied field of study. While requirements vary from country to country, law schools in many countries require at least a master's degree. Second, while academia is by no means an exclusive club for those with impeccable grades, a strong academic record will be invaluable. Third, it is important to start building a portfolio of 'publishable' research. The faculty you apply to will be interested in seeing a genuine interest in producing research for publication. Take advantage of opportunities to contribute to school law journals or journals associated with a student law society. Finally, take advantage of the easy access to tutors, lecturers and professors that you have while at university. There are plenty of friendly academics, not just in the law faculty, who will be happy to discuss potential career paths with you, and mentor you along your journey.",
})


# ============================================================================
# A12 - In-House Law
# ============================================================================

EDU_MODAL = "The College of Law offers a Master of Laws (Applied Law), through which you may specialise in In-House Practice. The courses deal with the commercial aspects of being an in-house lawyer and include areas such as dispute and project management.\n\nMore information: https://www.collaw.edu.au/campaigns/PG/in-house-practice-postgraduate-programs-course-guide/"

MEL_STOREY = "When I first decided to pursue a career in law, I wasn't exactly plotting a grand entrance into the in-house legal world. I didn't even know what \"in-house\" meant! I just loved the intellectual challenge, the idea of solving complex puzzles (and frankly, the dramahhh), so law school felt like the natural fit. I figured I would sort the rest out later. Fast-forward a few years and there I was, working in 'Big Law'. The suits, the billable hours, the constant emails (so many emails!) - it wasn't as glamorous as TV dramas make it look.\n\nI realised my passion for law needed more than just isolated contract reviews without a lot of context, multiple layers between me and the client, or endless hours of due diligence.\n\nI wanted to use my legal skills to actually move the needle, to shape strategy, and yes, sometimes even throw in a little personality and humour when I could.\n\nThat's when I found my sweet spot - working as an in-house lawyer. In-house suits my personality and learning style perfectly. I thrive in environments where I can mix legal expertise with business strategy. I'm not just looking at the legal implications of a decision, I'm asking how it fits into the bigger picture. I'm working with stakeholders from all across the business and am surrounded by lots of different professionals - not just lawyers.\n\nI can make a difference by providing practical solutions, not just black-and-white legal advice. I've always believed that lawyers can be problem-solvers and not just rule-keepers. Working in-house allows me to do exactly that. My advice to aspiring in-house lawyers: take the initiative. Internships, networking, finding mentors - these are your best bets to break into the world of in-house law. Extra study is an option too to show your commitment to this style of practice. It's not for everyone. In-house legal leaders don't just want someone running away from the intensity of billable-hour life in private practice; they want someone genuinely interested in the business and the industry.\n\nThroughout my career, I've had opportunities I never imagined, from working with international teams, travelling all over the world, to launching \"The Counsel Podcast\" (and an adjacent personal brand online) where I get to interview brilliant in-house lawyers and share their stories with the world.\n\nMy podcast passion project has been incredibly rewarding, giving me a platform to demystify what it's like to be an in-house lawyer and offering advice for those looking to follow the same path. I always want to provide the resources I wish I had available to me when I was earlier in my career.\n\n**What's required to join the in-house world?**\n\nA solid legal background is a must, but beyond that, you need to be adaptable, business-savvy, and excellent at communicating with all levels of a company and external stakeholders. The ability to understand the \"business speak\" alongside the legal jargon is key to thriving here. You also have to be comfortable with ambiguity - sometimes, there's no textbook answer and your business stakeholders may look to you for your best advice on the facts, or your 'gut feel' based on experience and pattern recognition of what can go wrong but also, how to mitigate the risk.\n\n**The most rewarding aspect of working in-house?**\n\nSeeing how my legal advice helps shape a company's decisions. I'm not just reacting, I'm actively contributing to the direction of the business. And the cherry on top? I get to do all of this without clocking a single billable unit. ALL of my time at work is considered to be \"billable\".\n\n**One misconception I encounter frequently?**\n\nOmg. Heaps!!! That in-house lawyers are just \"the department of no\". We're not here to shut things down, we're here to enable progress while keeping things on track. We offer practical solutions, not just \"no's.\"\n\nFor any law students still figuring out their path, my advice is simple: try different things.\n\nPractice in various areas of law (I always say that no experience is ever wasted and you won't pigeon-hole yourself in early, I promise!), ask LOTS of questions, and don't be afraid to take the road less travelled. Your journey doesn't have to be linear, and the legal world has more options than you probably have been led to think thanks to TV dramas and slick big law firm advertising on campus.\n\nIn-house law is challenging, dynamic, and incredibly rewarding. If you're up for the adventure and 'knowing a little bit about a lot', it might just be the perfect fit for you. Try it and see (you can always go back to conventional private practice - but you probably won't ;)).\n\nPlease see more of Mel's excellent content here: https://linktr.ee/theinhouselawyer"

write("in-house-law", {
    "slug": "in-house-law",
    "name": "In-House Law",
    "iconName": "building-2",
    "status": "published",
    "sections": [
        {
            "displayMode": "buttonRow",
            "orgs": [
                {"slug": "in-house-edu", "name": "Further Educational Opportunities", "pathways": ["in-house-law"], "links": [{"label": "Further Educational Opportunities", "type": "resource-modal", "modalContent": EDU_MODAL}]},
                {"slug": "mel-storey", "name": "At Home in House", "pathways": ["in-house-law"], "links": [{"label": "At Home in House (Mel Storey)", "type": "resource-modal", "modalContent": MEL_STOREY, "byline": "By Mel Storey"}]},
            ],
        }
    ],
    "bodyContent": "## What is an In-House Lawyer?\n\nMany organisations will employ legal counsel to work solely for the firm. The type of work will vary depending on the nature of the organisation, but can include contract law, company secretarial work, regulatory approval and compliance, banking and securities law, protection of intellectual property, employment law, or consumer law.\n\nThe experience of working in-house is one that is entirely distinct from working within a law firm. In-house practitioners often benefit from flexible working hours, an opportunity to participate in business decision making, an absence of billable quotas and a favourable work-life balance.\n\nIn addition, research by the Australian Corporate Lawyers Association has shown that 80% of in-house lawyers receive value-added benefits: 57% receive a bonus, 22% receive superannuation greater than the employer compulsory contribution, and 3% receive fringe benefits tax benefits associated with working for a charity.\n\n## Pathways to In-House Legal Work\n\nGenerally, lawyers who work in-house are already qualified to practise as solicitors and have extensive industry experience. In-house solicitors often start out in a law firm doing corporate and commercial legal work, before moving to an internal legal team. Many law firms also provide experienced legal counsel and provide graduates with opportunities to undertake secondments within in-house teams. Although many organisations have in-house legal departments, very few offer graduate-level positions. Employment positions are generally advertised on the organisation's website and secondments are usually arranged internally.\n\n## Who represents In-House Lawyers?\n\nThe Association of Corporate Counsel Australia ('ACCA') is the peak body for in-house lawyers. They host events, conferences, training workshops, and even have a yearly mentoring programme, which pairs less experienced in-house lawyers with mentors from a different industry sector. More information: http://acla.acc.com/",
})


# ============================================================================
# A13 - The Bar
# ============================================================================

BAR_MODAL = "## Barrister's Work Experience Program\n\nRun by the UQLA. Successful applicants shadow a barrister for two days, usually in September. https://www.uqla.org.au/work-experience\n\n## Job as a Barrister's Assistant or Secretary\n\nBuild contacts in the industry through networking or keep an eye out for advertised roles on popular job websites."

write("the-bar", {
    "slug": "the-bar",
    "name": "The Bar",
    "iconName": "mic",
    "status": "published",
    "sections": [
        {
            "displayMode": "buttonRow",
            "orgs": [{"slug": "bar-opportunities", "name": "Opportunities for Students", "pathways": ["the-bar"], "links": [{"label": "Opportunities for Students", "type": "modal", "modalContent": BAR_MODAL}]}],
        }
    ],
    "bodyContent": "## What is a Barrister?\n\nIn Queensland, there is a division between the work of solicitors and barristers. A barrister is a specialist advocate who appears before Courts and Tribunals and is an 'Officer of the Court' who practises independently. Typically, barristers working at the private bar accept instructions from solicitors, including those employed by Crown Law, and act for clients in matters that reflect their interest and expertise. Barristers may also be employed by government departments including the Office of the Director of Public Prosecutions or Legal Aid Australia. Barristers are often called upon to give legal advice and assist with dispute resolution. An increasing number of barristers are now specialising in Alternative Dispute Resolution and arbitration. Furthermore, barristers can become involved in law reform and pro bono work through the Bar Association of Queensland.\n\n## Pathways to the Bar\n\nIn Queensland, the Bar is regulated by the Rules of the Bar Association of Queensland. Like solicitors, barristers are required to have a law degree (either the Bachelor of Laws or the Juris Doctor). They must also complete the Practical Legal Training ('PLT') course and be admitted to the legal profession, at which point they receive a solicitor's practising certificate. At this point, a barrister-to-be's path diverges from that of a solicitor. Bar Exams must be undertaken, which cover areas such as legal ethics, practice and procedure, and evidence. Once you pass the exams, you may commence the Bar Practice Course, which runs for six weeks. Both the Exams and the Course are offered through the Bar Association of Queensland.",
    "relatedPathways": ["criminal-law", "legal-aid-queensland", "government-and-public-service"],
})


# ============================================================================
# A14 - Legal Technology (coming soon)
# ============================================================================

write("legal-technology", {
    "slug": "legal-technology",
    "name": "Legal Technology",
    "iconName": "cpu",
    "status": "coming-soon",
    "sections": [],
    "bodyContent": "## Coming soon\n\nWe're putting together content on legal technology careers. In the meantime, explore [Boutique & Other Specialties](/pathways/boutique-and-other-specialties/) and [In-House Law](/pathways/in-house-law/) for adjacent practice areas.",
})

write("pro-bono-commercial-firms", {
    "slug": "pro-bono-commercial-firms",
    "name": "Pro Bono Within Commercial Firms",
    "iconName": "hands-praying",
    "status": "coming-soon",
    "sections": [],
    "bodyContent": "## Coming soon\n\nThis pathway will cover pro bono practice within mid- and top-tier commercial firms. In the meantime, see [Community Legal Centres](/pathways/community-legal-centres/) and [JATL Recommends](/resources/jatl-recommends/).",
})

print("All pathway JSON files generated.")
