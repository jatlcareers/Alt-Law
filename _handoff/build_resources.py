"""Generate all resource JSON files from CONTENT.md (one-time build script)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "content", "resources")
os.makedirs(OUT, exist_ok=True)

def write(slug, data):
    with open(os.path.join(OUT, f"{slug}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"wrote {slug}.json")


# B1.1 Job Search
write("job-search", {
    "slug": "job-search",
    "category": "resources-and-guides",
    "title": "Job Search",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "Job Boards",
            "body": "As you transition from university to your career, exploring graduate employment options is crucial. These roles are tailored for recent graduates and are available through a range of organisations - including government bodies, private enterprises, and non-profit groups - that aim to empower newcomers in their professional lives.\n\nGraduate jobs typically provide structured training, mentoring, and ongoing support, enabling you to apply your academic knowledge in real-world settings. They offer a valuable starting point for a lasting career, helping you gain practical industry experience, build your network, and make impactful contributions within your chosen area.\n\n*Remember: set up job alerts with these websites through your email to not miss out on opportunities suited to you!*",
        },
        {
            "type": "links",
            "heading": "Internships, graduate programs and graduate jobs",
            "links": [
                {"label": "Seek Graduate Jobs", "href": "https://www.seek.com.au/graduate-jobs"},
                {"label": "Prosple", "href": "https://au.prosple.com/search-jobs?study_fields=655&keywords&defaults_applied=1&location=Australia", "description": "Early-careers job board; graduate programs and jobs with government and private organisations."},
                {"label": "Indeed Graduate Jobs", "href": "https://au.indeed.com/q-graduate-jobs.html"},
                {"label": "QLD Government Graduate Portal", "href": "https://www.qld.gov.au/jobs/graduate-portal/graduate-programs"},
                {"label": "Australian Government Graduate Program", "href": "https://www.naa.gov.au/about-us/employment/entry-level-programs/australian-government-graduate-program"},
                {"label": "Australian Public Service graduate and entry level programs", "href": "https://www.apsc.gov.au/about-us/working-commission/apsc-graduate-opportunities"},
            ],
        },
        {
            "type": "links",
            "heading": "General Job Search",
            "links": [
                {"label": "SEEK", "href": "https://www.seek.com.au/"},
                {"label": "CareerOne", "href": "https://www.careerone.com.au/"},
                {"label": "Jora", "href": "https://au.jora.com/"},
                {"label": "Indeed", "href": "https://au.indeed.com/"},
                {"label": "Workforce Australia", "href": "https://www.workforceaustralia.gov.au/individuals/"},
                {"label": "Australian Public Service Jobs", "href": "https://www.apsjobs.gov.au/s/"},
                {"label": "SmartJobs", "href": "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.searchResults", "description": "Queensland Government jobs."},
                {"label": "LinkedIn Job Search", "href": "https://www.linkedin.com/jobs/search/"},
            ],
        },
        {
            "type": "links",
            "heading": "Law Specific",
            "links": [
                {"label": "The College of Law Jobs Board", "href": "https://jobs.collaw.com/", "description": "Sponsor."},
                {"label": "EthicalJobs", "href": "https://www.ethicaljobs.com.au/jobs?locations=5%2C6&categories=35", "description": "Careers in social-justice / social-equity / environmental sustainability orgs."},
                {"label": "Legal Careers", "href": "https://www.legalcareers.com.au/"},
                {"label": "Law Staff", "href": "https://www.lawstaff.com.au/"},
            ],
        },
        {
            "type": "prose",
            "heading": "UQ student-only resources",
            "body": "All UQ students can access job listings, advice and services:",
            "links": [
                {"label": "UQ Career Hub", "href": "https://studenthub.uq.edu.au/students/login", "meta": "Login required", "description": "Job vacancies from employers, locally and internationally."},
                {"label": "UQ Union job preparation service", "href": "https://www.uqu.com.au/student-support/job-preparation", "description": "Helps students find and apply for casual jobs."},
                {"label": "UQ's Careers and Employability office", "href": "https://study.uq.edu.au/enhance-your-employability", "description": "Job searching, networking, and application writing."},
            ],
        },
        {
            "type": "links",
            "heading": "Career advice",
            "intro": "*Both Prosple and EthicalJobs feature pages dedicated to career advice and help with your job application. Please also have a look at these pages to learn more and evaluate your resources:*",
            "links": [
                {"label": "Prosple - Graduate Law Careers Advice", "href": "https://au.prosple.com/law"},
                {"label": "Prosple - Community Forum", "href": "https://forum.prosple.com/categories", "expandable": "Review FAQs or ask a question about internships or graduate roles and get honest advice from grads, peers and employers."},
                {"label": "EthicalJobs - Career Advice", "href": "https://www.ethicaljobs.com.au/blog", "expandable": "Not only features materials on searching for a job and workplace wellbeing and development, but also offers more niche advice catered to values-based careers and organisations, such as volunteering opportunities and job trends in sustainable industries/workplaces."},
            ],
        },
    ],
    "relatedResources": ["external-resources", "career-support"],
})


# B1.2 Career Support
write("career-support", {
    "slug": "career-support",
    "category": "resources-and-guides",
    "title": "Career Support",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "My Career Adviser",
            "body": "My Career Adviser (MCA) is an online flexible career development and employability learning resource. MCA provides a vast array of audio-visual materials (including video content), readings, web pages, modules, and mini-assessments, including Capstone Projects (self, reflective, and automated).\n\nOnce you are enrolled in MCA, you can locate the platform in Blackboard (learn.uq) under the 'Organisations' tab. Expect diverse topics, useful resources and engaging activities.",
            "links": [
                {"label": "Sign Up today", "href": "https://employability.uq.edu.au/career-development/my-career-adviser"},
                {"label": "Career Action Planning: Your professional roadmap", "href": "https://employability.uq.edu.au/files/179264/SEED-Careers-Factsheet-CareerActionPlan%20-%20FINAL.pdf", "meta": "PDF", "description": "A great reflective activity."},
            ],
        },
        {
            "type": "prose",
            "heading": "The Business, Economics and Law (BEL) Careers and Employability team",
            "body": "The BEL Careers and Employability team provides resources, advice, industry insights and work placement opportunities just for BEL students. Tools, events and activities to help you explore your career options, develop your capabilities, and build your professional profile and networks.\n\nNeed to talk to someone in person? Book a face-to-face or online consultation with a BEL Careers Advisor.",
            "links": [
                {"label": "Book a Career Consult in StudentHub", "href": "https://studenthub.uq.edu.au/students/appointments/app/topic/243?siteId=1"},
            ],
        },
        {
            "type": "prose",
            "heading": "Attend an event",
            "body": "From application writing, professional identity, and interviewing workshops, to networking, career planning and learning about workplace culture, the workshops and events provided by UQ will help you to build capabilities that will make you more employable no matter what direction you choose to take your career in.",
            "links": [
                {"label": "UQ Career Development Workshops and Events", "href": "https://employability.uq.edu.au/career-development/events"},
            ],
        },
        {
            "type": "contact",
            "heading": "Contact the team today",
            "email": "careers@bel.uq.edu.au",
            "phone": "+61 7 3365 4222",
            "hours": "8:30am to 4:00pm, Monday to Friday",
            "address": {"label": "Colin Clark Courtyard, Room 107", "mapHref": "https://maps.uq.edu.au/?campusId=406&zLevel=1&zoom=18&identifier=538231f9483bd3bda1d14980a8f19885175bf94459fd824878cffeaac09a037d"},
            "social": [
                {"platform": "Instagram", "handle": "@uqbelstudentlife", "href": "https://www.instagram.com/uqbelstudentlife/"},
            ],
        },
    ],
})


# B1.3 External Resources
write("external-resources", {
    "slug": "external-resources",
    "category": "resources-and-guides",
    "title": "External Resources",
    "status": "published",
    "intro": "*We'd like to highlight some excellent careers resources for law students outside university from our sponsors:*",
    "buttons": [
        {
            "label": "College of Law",
            "type": "resource-modal",
            "modalContent": "Alongside the excellent content around completing your PLT, College of Law also offers other excellent resources for students, including:\n\n- [Practical Legal Training (PLT) guide](https://www.collaw.edu.au/practical-legal-training/) - access either a general PDF guide or a tailored version emailed to you to shape your own PLT plan suited to you.\n- [Alternative Careers Guide](https://www.collaw.edu.au/practical-legal-training/alternative-careers) - College of Law's careers guide for students and graduates exploring legal career options beyond private practice or in-house roles.\n- [How to Become a Lawyer (PDF)](https://vfpsua.files.cmp.optimizely.com/download/assets/How+to+become+a+lawyer+SEP24.pdf/fcff873ad1d911ee87658ee96f755a99) - step-by-step overview of the pathway to admission in Australia.\n- [Jobs Board](https://jobs.collaw.com/jobs/) - PLT placements and early-career roles for both law students and graduates.\n- [News, Resources and Events](https://www.collaw.edu.au/community/) - graduate interviews, short video learning materials and articles.",
        },
        {
            "label": "Queensland Law Society (QLS)",
            "type": "resource-modal",
            "modalContent": "QLS organises their resources and events tailored to students and early career professionals on their website under [The Hub: Early Career Lawyers](https://www.qls.com.au/the-hub-early-career-lawyers). Some of the incredible resources we'd like to highlight include:\n\n- [QLS Student Membership](https://www.qls.com.au/qls-membership/student-membership) - access valuable resources for study, career, professional and social networks, and exclusive member discounts.\n- [Legal Careers Expo](https://www.qls.com.au/the-hub-early-career-lawyers/legal-careers-expo) - yearly networking event for Queensland law students; direct access to employers, practical career advice, LinkedIn Rescue, professional headshots.\n- [The Callover](https://www.qls.com.au/the-hub-early-career-lawyers/the-callover) - QLS podcast created by young lawyers, for young lawyers.\n- [Your Legal Career](https://www.qls.com.au/the-hub-early-career-lawyers/your-legal-career) - resources and assistance for different stages between studying law and admission.\n- [QLS Proctor - Law Students](https://www.qlsproctor.com.au/category/people/law-students/) - articles from QLS Proctor tailored to law students.",
        },
    ],
    "sections": [],
    "relatedResources": ["job-search"],
})


# B1.4 Resumes
write("resumes", {
    "slug": "resumes",
    "category": "resources-and-guides",
    "title": "Resumes",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "VMock Resume tool",
            "body": "VMock Smart Resume is an AI-powered tool that gives you instant, personalised feedback on your resume and lets you tailor it to a specific job opportunity you're interested in. Access it anytime, anywhere to receive tailored improvement suggestions or choose from professional templates that help your resume stand out.",
            "links": [
                {"label": "Sign up to VMock", "href": "https://employability.uq.edu.au/get-the-edge/faculty-programs/bel/vmock-resume-tool"},
            ],
        },
        {
            "type": "prose",
            "heading": "Crafting a Resume",
            "subheading": "BEL Employability Essentials module",
            "body": "Your resume is a key part of your job application. It shows your qualifications, experience, skills and accomplishments, and if done well, will help you get a job interview.\n\nIn this module, you'll learn how to create a resume that:\n\n- looks professional\n- highlights your strengths\n- matches the requirements of a specific job.",
            "links": [
                {"label": "'Crafting a Resume' module", "href": "https://rise.articulate.com/share/xfDhWh0J_km4BJ7w87JVtVCMjyQefIQX#/"},
                {"label": "Resume and cover letter writing guide", "href": "https://studenthub.uq.edu.au/docs/408/Resume-Help.pdf", "meta": "PDF, 127.8 KB"},
                {"label": "Top tips for writing your resume", "href": "https://employability.uq.edu.au/files/179529/SEED-Careers-ResumeTips2022.pdf", "meta": "PDF, 49.3 KB"},
                {"label": "Resume Checklist", "href": "https://employability.uq.edu.au/files/179903/SEED-Careers-ResumeChecklist2022.pdf", "meta": "PDF, 50.5 KB"},
            ],
        },
    ],
    "relatedResources": ["cover-letters", "preparing-for-applications"],
})


# B1.5 Cover Letters
write("cover-letters", {
    "slug": "cover-letters",
    "category": "resources-and-guides",
    "title": "Cover Letters",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "Writing a Cover Letter",
            "subheading": "BEL Employability Essentials module",
            "body": "A cover letter is part of your personal marketing toolkit. A strong cover letter can improve your chances of being shortlisted for an interview.\n\nIn this module you'll learn how to:\n\n- understand what employers look for in cover letters\n- highlight your skills and experience clearly and briefly\n- write a strong cover letter that helps you secure an interview.",
            "links": [
                {"label": "'Writing a Cover Letter' module", "href": "https://rise.articulate.com/share/LqGHN43nkkBD0uaksgv1Ys9xMwJ5bLJh#/"},
                {"label": "Resume and cover letter writing guide", "href": "https://studenthub.uq.edu.au/docs/408/Resume-Help.pdf", "meta": "PDF, 127.8 KB"},
                {"label": "Top tips for writing your cover letter", "href": "https://employability.uq.edu.au/files/179534/SEED-Careers-CoverLetterTips2022.pdf", "meta": "PDF, 57.6 KB"},
                {"label": "Cover Letter Checklist", "href": "https://employability.uq.edu.au/files/179898/SEED-Careers-CoverLetterChecklist2022.pdf", "meta": "PDF, 46.9 KB"},
                {"label": "The words to use in your application - Action verbs", "href": "https://employability.uq.edu.au/files/208129/SES%20-%20Careers%20-%20Action%20Verbs%20-%202025.pdf", "meta": "PDF, 77.6 KB"},
                {"label": "Choosing referees", "href": "https://employability.uq.edu.au/files/201263/Referees%20Guide.pdf", "meta": "PDF"},
            ],
        },
        {
            "type": "links",
            "heading": "Selection Criteria",
            "links": [
                {"label": "Top tips for writing your selection criteria", "href": "https://employability.uq.edu.au/files/179539/SEED-Careers-SelectionCriteriaTips2022.pdf", "meta": "PDF, 47.5 KB"},
            ],
        },
    ],
    "relatedResources": ["resumes", "preparing-for-applications"],
})


# B2.1 Preparing for Applications
write("preparing-for-applications", {
    "slug": "preparing-for-applications",
    "category": "networking-interviews-recruitment",
    "title": "Preparing for Applications",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "Understand",
            "body": "Written applications may encompass a range of different stages and documents including cover letters, resumes and selection criteria.\n\nUnderstanding the purpose and strategies behind a successful application is a valuable capability to develop as it will support you well into your career. Whether you have never written a professional application before or you are looking to make final adjustments to your tailored application, support is available on your journey. These resources will help you to be better equipped to communicate your strengths and meet the expectations of potential employers.",
            "links": [
                {"label": "UQ Career Development Workshops and Events", "href": "https://employability.uq.edu.au/career-development/events"},
            ],
        },
        {
            "type": "prose",
            "heading": "Prepare",
            "body": "Are you preparing your written application or preparing for your interview? One of the key places to start is reflecting on your academic pathway, employment history and broader experiences and then considering how to articulate your competencies. Unpacking and articulating your experiences is essential to show your value to prospective employers.",
            "links": [
                {"label": "Unpacking and articulating your experiences", "href": "https://employability.uq.edu.au/files/186260/SES%20-%20Careers%20-%20Articulating%20Your%20Experiences%20-%202025.pdf", "meta": "PDF"},
            ],
        },
        {
            "type": "prose",
            "heading": "STAR (Situation-Task-Action-Result)",
            "body": "The STAR method is a structured manner of responding to selection criteria as well as 'behavioural-based' or 'competency-focused' interview questions. The STAR Template will walk you through the steps of unpacking your experiences and effectively hone your skill using the STAR approach.",
            "links": [
                {"label": "STAR Template", "href": "https://employability.uq.edu.au/files/200784/STAR%20template.pdf", "meta": "PDF"},
            ],
        },
        {
            "type": "prose",
            "heading": "SEAL (Situation-Experience-Action-Learning)",
            "body": "Similar to STAR, SEAL assists students to articulate what you have learnt from an experience.",
            "links": [
                {"label": "SEAL Reflection Method template", "href": "https://employability.uq.edu.au/files/179389/SEED-Careers-SEAL2022.pdf", "meta": "PDF"},
            ],
        },
        {
            "type": "prose",
            "heading": "Unpacking the role",
            "body": "Jobs can be complicated when they are broken down from their title into individual roles and responsibilities. Unpacking the role is a strategic approach that helps you:\n\n- Filter out roles you don't want to apply for\n- Research the role and organisation\n- Identify key words and ideas for your application",
            "links": [
                {"label": "Unpacking the role", "href": "https://employability.uq.edu.au/files/207959/SES%20-%20Careers%20-%20Unpack%20the%20Role%20-%202025.pdf", "meta": "PDF"},
            ],
        },
        {
            "type": "prose",
            "heading": "EMPLOY101x",
            "body": "EMPLOY101x \"Unlocking your employability\" is a self-paced, online course based on UQ's approach to student employability development. The course provides strategies and techniques to help you to learn from your experiences, identify your unique capabilities and attributes, and effectively communicate your employability in different contexts, such as in the recruitment process and through pitching.\n\nWith examples from different industries and environments, and contributions from employers, entrepreneurs, students, graduates and experts, this course will help prepare you to navigate the unpredictability of the world of work, both now and throughout your career.\n\nUQ students can access the full and free version of the course by using their UQ student email to register and enrol and using the voucher code: **E21U49M2B38SBV4N**. Instructions at the link below will step you through registration in the course.\n\nIf you have any questions regarding accessing the verified version of the course contact employ@uq.edu.au.",
            "links": [
                {"label": "EMPLOY101x \"Unlocking your employability\"", "href": "https://www.edx.org/course/unlocking-employability-uqx-employ101x-0"},
                {"label": "UQ enrolment instructions", "href": "https://learn.uq.edu.au/ultra/courses/_185094_1/cl/outline"},
            ],
        },
        {
            "type": "prose",
            "heading": "Employability Award",
            "body": "The Employability Award program is a structured program that recognises the personal and professional development you can gain from your involvement in activities above and beyond your academic studies. It is essentially a learning program that will guide you through a range of experiences and reflections to unlock your potential.",
            "links": [
                {"label": "Employability Award", "href": "https://employability.uq.edu.au/award"},
            ],
        },
    ],
    "relatedResources": ["resumes", "cover-letters", "job-interviews"],
})


# B2.2 Job Interviews
write("job-interviews", {
    "slug": "job-interviews",
    "category": "networking-interviews-recruitment",
    "title": "Job Interviews",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "Preparing for an Interview",
            "subheading": "BEL Employability Essentials module",
            "body": "The interview is one of the most important stages of the recruitment process. How well you prepare and present yourself can make a big difference to your success.\n\nThis module will:\n\n- give you insights into what to expect from different interview types\n- help you prepare clear and confident answers\n- build confidence and help you communicate your message effectively.",
            "links": [
                {"label": "'Preparing for an Interview' module", "href": "https://rise.articulate.com/share/wtRlfow7GaYpm5OkO5HVnT140W0NQdzj"},
            ],
        },
        {
            "type": "prose",
            "heading": "Interview prep resources",
            "body": "Most recruiters use interviews as the main method to screen candidates.\n\nPanels usually ask scenario-based and technical questions to assess fit. Answering professionally using the STAR technique is an effective way to respond. The Interview Questions Bank for the New Colombo Plan helps demonstrate STAR in action and can provide a handy guide when structuring your approach to anticipated questions.\n\nThe Interview guide and checklist and Interview Questions worksheet are some handy resources for preparation.",
            "links": [
                {"label": "STAR template", "href": "https://employability.uq.edu.au/files/179384/SEED-Careers-STARE_Template2022.pdf", "meta": "PDF"},
                {"label": "Interview Questions Bank for the New Colombo Plan", "href": "https://employability.uq.edu.au/files/201264/Interview%20Questions%20NCP.pdf", "meta": "PDF"},
                {"label": "Interview guide and checklist", "href": "https://employability.uq.edu.au/files/179664/SEED-Careers-InterviewChecklist2022.pdf", "meta": "PDF"},
                {"label": "Interview Questions worksheet", "href": "https://employability.uq.edu.au/files/201254/Interview%20questions%20bank.pdf", "meta": "PDF"},
            ],
        },
        {
            "type": "prose",
            "heading": "Workshops & Programs",
            "body": "UQ students can access a range of workshops to help you hone your approach to interviews.\n\nThe Employability Award program is a structured program that recognises the personal and professional development you can gain from your involvement in activities above and beyond your academic studies. It is essentially a learning program that will guide you through a range of experiences and reflections to unlock your potential.",
            "links": [
                {"label": "UQ Career Development Workshops and Events", "href": "https://employability.uq.edu.au/career-development/events"},
                {"label": "Employability Award", "href": "https://employability.uq.edu.au/award"},
            ],
        },
    ],
    "relatedResources": ["preparing-for-applications", "understand-the-recruitment-process"],
})


# B2.3 Recruitment Process
write("understand-the-recruitment-process", {
    "slug": "understand-the-recruitment-process",
    "category": "networking-interviews-recruitment",
    "title": "Understand and Navigate the Recruitment Process",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "UQ Business, Economics and Law Faculty - Recruitment Ready Program",
            "body": "Recruitment Ready helps Business, Economics and Law (BEL) students understand real-world recruitment processes and build the skills needed for competitive applications. Delivered every semester in collaboration with an industry partner, the program gives you hands-on experience in how employers assess candidates for internships, vacation programs and graduate roles.\n\nThe Recruitment Ready program will help you develop practical insights into:\n\n- what to expect from a real recruitment process\n- the behaviours, attributes and professional skills employers look for\n- how to stand out and communicate your value confidently\n- how to present professionally, in writing and in person\n- how to reflect on feedback and improve for future applications\n\nOver just a few weeks, you'll gain a clear understanding of the recruitment process - from submitting applications to interviewing - while practising the skills employers value most. The program is designed for mid-degree students and is best completed before applying for work experience or employment opportunities.",
            "links": [
                {"label": "Find out more and apply", "href": "https://employability.uq.edu.au/get-the-edge/faculty-programs/bel/recruitment-ready"},
            ],
        },
        {
            "type": "prose",
            "heading": "Navigate the Recruitment Process",
            "subheading": "BEL Employability Essentials module",
            "body": "Applying for graduate roles can be exciting but it can also feel complex and overwhelming. Knowing how the process works will help you stay organised and improve your chances of success.\n\nIn this module you'll learn how to:\n\n- understand the difference between graduate programs and graduate roles\n- recognise the key stages of the recruitment process\n- track and manage your job applications.",
            "links": [
                {"label": "'Navigating the recruitment process' module", "href": "https://rise.articulate.com/share/GMvB8eiP-6b6ZwTXTnwpzs6MsTQCBeya"},
            ],
        },
    ],
})


# B2.4 Get Workplace Ready
write("get-workplace-ready", {
    "slug": "get-workplace-ready",
    "category": "networking-interviews-recruitment",
    "title": "Get Workplace Ready",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "Preparing for the workplace",
            "subheading": "BEL Careers and Employability module",
            "body": "Preparing for the workplace helps you build a strong foundation for your career. Preparation allows you to adapt to new environments and meet employer expectations with confidence.\n\nIn this module you'll gain:\n\n- clear guidance on workplace expectations\n- practical communication skills\n- an understanding of professional behaviour and etiquette.",
            "links": [
                {"label": "'Preparing for the workplace' module", "href": "https://rise.articulate.com/share/S-lLqPadEr4YJJCqOvW-L5lIIZ6nZnIF#/"},
            ],
        },
    ],
})


# B2.5 Get Experience
write("get-experience", {
    "slug": "get-experience",
    "category": "networking-interviews-recruitment",
    "title": "Get Experience",
    "status": "published",
    "sections": [
        {
            "type": "prose",
            "heading": "Work-integrated Learning (WIL)",
            "body": "Gain hands-on experience that counts towards your degree through Work-integrated Learning (WIL) internships and consultancy projects.\n\nThese electives boost your employability by developing:\n\n- professional networks and industry insights\n- an awareness of workplace culture and expectations\n- experiences for your CV/job application\n- transferable skills for a multitude of positions.\n\nTurn your knowledge into practical experience working in business, economics or law with a Work-integrated Learning (WIL) student placement (internship). Earn academic credit while practising your future profession, networking with future peers and learning from industry leaders.",
        },
        {
            "type": "prose",
            "heading": "Internships",
            "body": "The Law School offers selected students in the Bachelor of Laws (Hons) and dual degree programs the opportunity to gain practical legal experience in a professional setting. (LAWS5114)",
            "links": [
                {"label": "Learn about Legal Education placements and apply"},
                {"label": "BEL Internship Guide"},
                {"label": "UQ Industry Partners"},
                {"label": "Check StudentHub for new opportunities"},
            ],
        },
        {
            "type": "contact",
            "heading": "Help is available",
            "intro": "Book a consult with a WIL Advisor.",
            "email": "employability@bel.uq.edu.au",
        },
    ],
})


# B3.1 Personal Branding and Networking Tips
write("personal-branding-and-networking-tips", {
    "slug": "personal-branding-and-networking-tips",
    "category": "jatl-career-tips",
    "title": "Personal Branding and Networking Tips",
    "status": "published",
    "byJatl": True,
    "sections": [
        {
            "type": "prose",
            "heading": "Professional Branding and Networking Strategy",
            "body": "Having a clear understanding of your personal value proposition (also referred to as your professional brand) and developing strategies to connect and network with industry, is vital when carving out your career pathway. This worksheet has been created to walk you through the process of developing and/or refining your professional branding and networking strategy to set you up for success. Understanding and communicating your professional values and developing a unique value proposition is all part of the preparation.\n\nDo you google people? You can bet prospective employers will google you - some have quite sophisticated tools for this as part of their due diligence processes. Time to review your online activity and brand. Consider a Social Media Audit.",
        },
        {
            "type": "prose",
            "heading": "Your Elevator Pitch",
            "body": "An Elevator Pitch is a brief, persuasive speech that you may utilise to introduce yourself and articulate your value to a prospective employer or organisation. They may be useful for engaging with industry and peers at networking events, at job interviews or even in a workplace at the water cooler. Your elevator pitch will depend on the person or organisation that you are meeting, and it may be useful to develop a range of pitches depending upon the context and person. It is recommended for an effective Elevator Pitch to not exceed 1 minute.",
            "links": [
                {"label": "Developing and refining your elevator pitch", "meta": "PDF, 61.9 KB"},
            ],
        },
        {
            "type": "prose",
            "heading": "Networking Events",
            "body": "BEL networking events connect students planning a WIL internship course with industry professionals seeking interns.\n\nAdditionally, Queensland Law Society holds a number of networking events targeted at students, graduates and other young professionals in the Queensland legal profession. Two major ones we'd like to highlight are:\n\n- **Better Call Sarah**\n- **Legal Expo** - the premier careers fair for law students in Queensland\n\nKeep an eye out on social media for different panels and networking events held by JATL, along with other Brisbane student law societies (i.e. UQLS, QUT Law, Innovation & Technology, etc.).",
            "links": [
                {"label": "Legal Careers Expo (QLS)", "href": "https://www.qls.com.au/the-hub-early-career-lawyers/legal-careers-expo"},
                {"label": "BEL Careers and Networking Events"},
            ],
        },
        {
            "type": "prose",
            "heading": "Networking: Our Advice",
            "body": "Being nervous and anxious when attending a networking event, especially when you're young and/or new to networking with professionals, is completely normal. Networking has quite a bad reputation for being just an opportunity to make transactional relationships and promote your ego. But we disagree. Networking gives you the chance just to talk to people and actually learn more about them and their job. Park your \"law student overthinking\" instincts and try to relax and take an approach of just learning about people and their job: you don't need to prove yourself to anyone. If someone does act rude or facetious, it probably comes from the same fear around networking and needing to prove you're good enough. It sounds basic, but just asking the questions you want to ask and actively listening and responding to someone's answers will likely be enough to continue the flow of conversation and make a good impact on someone.\n\nDon't let imposter syndrome get in the way. Try to just be genuine, interested and respectful and you will be good enough at networking. If you feel uncomfortable, take a minute to grab some water or food and do some controlled breathing. If you can, invite along a buddy (or find someone you know at the event, even if they're just an acquaintance) and tackle networking together as a team. This can really help with boosting your confidence when you're starting out at networking events and can help to make some of the initially awkward bits (joining a conversation, asking for someone's LinkedIn, keeping the conversation flowing, etc.) a lot easier. Sometimes, even assigning roles to each other (i.e. I'll ask these questions, you're remembering to ask for LinkedIn details at the end, etc.) can help you out. Whatever method works best for you and makes you feel comfortable will work. Remember: if you just demonstrate genuine interest in the other person, you're a lot better at networking than you think.\n\nAlso, if you see someone who looks like they want to join the conversation but they aren't prepared to interrupt, we recommend being polite and inviting them to join the conversation. Not only is it worth it just based on the act of kindness alone, but this can also demonstrate to the professional you're talking to key qualities of teamwork and compassion which many employers value.",
        },
        {
            "type": "prose",
            "heading": "Conversation Starters",
            "variant": "callout-tip",
            "body": "If you feel like you can't think of anything to say, or just want to ask a question to keep the conversation moving, here are some general ideas we recommend (please adapt and reword based on context, familiarity and appropriateness considering the person you're talking to):\n\n- What current challenges are you facing in your role/organisation?\n- How are you overcoming/addressing that?\n- Is this a usual challenge for your role/organisation to face?\n- Where do you see yourself in the future in terms of your career (either with or without your organisation)?\n- What sort of values or interests drove you to work in this role/organisation?\n- How did you start out as a graduate?\n- What are some narratives around the student/graduate \"best path\" that you don't agree with or wish you could change?\n- What are some lessons you've learned from practical experience working in the law, rather than from just law school?\n- What do you wish you could tell your younger self about the legal profession or finding your career path?\n- Did you always want to work in the position you are in?\n- What do you like most about the role/industry?\n- What do you like least about the role/industry?\n- What makes an applicant stand out at your organisation?\n- How would you describe the culture at your organisation?\n- How will the Olympics impact your future work (or, will it)?\n- How is GenAI impacting your role, if at all?\n- What skills will benefit your organisation in the future?",
        },
        {
            "type": "prose",
            "heading": "Networking Conversation Flow",
            "body": "Some general themes that a networking conversation usually follows are:\n\n**1. Introduction and joining conversation.** Look out for professionals who are talking to a group and just ask if you can have a chat or ask a few questions.\n\n**2. Discuss work insights and career options.** This is where you really hone in on questions about the person's job and their career progression. Lots of professionals will have prepared things to highlight to you in answering your questions. Take the chance to learn these, then build on them through further, more specific questions which relate to your own career/personal interests.\n\n**3. Future work opportunities (if applicable) and culture.** This is where you can evaluate your level of rapport with the other person in the conversation and just follow the flow. If you're looking for more to ask, try asking questions about the legal industry, their workplace culture or (where appropriate) some of their personal interests, with a potential tie to work-life balance if you're curious.\n\n**4. The Wrap-Up.** Finishing your conversation at a networking event can initially feel hard and awkward, but don't worry, you will be fine. Where you feel like the conversation has hit a natural end, or the person has covered most if not all of your questions, you're welcome to say a polite concluding statement (i.e. \"Well thank you so much for your time and answering my questions; I really got a lot out of our conversation,\" etc.). Make sure you ask if you can connect with that person on LinkedIn (assuming they have one - common courtesy is that they would usually say yes) and say a final goodbye/call for a future discussion. Don't feel bad because you want to network with other professionals - that's the point of networking. As long as you aren't rude or obviously deceptive (i.e. you excuse yourself to the bathroom, say you'll be right back and go immediately join another conversation with a \"more interesting\" professional - a critique this writer is referencing from experience...) then your conversation ender is fine.",
        },
    ],
    "relatedResources": ["information-interview-guide", "linkedin"],
})


# B3.2 Career Mentoring
write("career-mentoring", {
    "slug": "career-mentoring",
    "category": "jatl-career-tips",
    "title": "Career Mentoring",
    "status": "published",
    "byJatl": True,
    "sections": [
        {
            "type": "prose",
            "heading": "Career mentoring",
            "body": "Career mentoring is a one-to-one relationship in which an experienced professional voluntarily offers their knowledge, insight and encouragement to facilitate the learning and development of a current student. A good career mentoring relationship is professional and equal, recognising that both mentor and mentee can grow from the experience. A mentor does not guarantee success and will often play contradictory roles - sometimes offering advice and support, at other times posing challenging questions and sharing critical thoughts.",
            "links": [
                {"label": "BEL Career Mentoring Program", "href": "https://mentoring.app.uq.edu.au/p/p4/about"},
            ],
        },
        {
            "type": "prose",
            "heading": "GenAI as a career planning tool",
            "body": "Additionally, as a starting point, use GenAI to draft yourself a career plan: once you've developed some ideas about the industry or role you're interested in, write these down and let AI analyse these to give you a draft checklist and notes on actions to take whilst studying and/or upon graduation. Remember to double-check the accuracy of what has been generated and try to give as much detail as possible within your prompt, both in terms of the information the GenAI model has to work off as well as your prompt on the task.",
        },
    ],
    "relatedResources": ["information-interview-guide"],
})


# B3.3 LinkedIn
write("linkedin", {
    "slug": "linkedin",
    "category": "jatl-career-tips",
    "title": "LinkedIn",
    "status": "published",
    "byJatl": True,
    "sections": [
        {
            "type": "prose",
            "heading": "LinkedIn",
            "body": "Engaging on LinkedIn offers significant benefits for Law students looking to build their professional identity and expand their networks. By actively participating on the platform, students can connect with practising lawyers, alumni, and potential employers, gaining valuable insights into career pathways and industry expectations. Additionally, sharing achievements, interests, and relevant content can help establish credibility and showcase a unique value proposition, making students more visible to recruiters and enhancing opportunities for internships and graduate roles.",
            "links": [
                {"label": "Create a good LinkedIn profile", "href": "https://www.linkedin.com/help/linkedin/answer/a554351"},
            ],
        },
        {
            "type": "links",
            "heading": "Follow",
            "links": [
                {"label": "Queensland Law Society", "href": "https://www.linkedin.com/company/queensland-law-society/"},
                {"label": "UQ Justice and the Law Society", "href": "https://www.linkedin.com/company/uq-justice-and-the-law-society/"},
                {"label": "UQ Law School", "href": "https://www.linkedin.com/company/uq-law-school/"},
                {"label": "The College of Law", "href": "https://www.linkedin.com/school/the-college-of-law-australia/"},
            ],
        },
        {
            "type": "prose",
            "heading": "Who else to follow",
            "body": "**People who do the work you'd be interested in doing some day.** Use keywords based on what you're interested in and do a little research based on subjects you've really enjoyed or think you might have an interest in to follow experts and other professionals in that area.\n\n**Organisations who do the work you are interested in,** including CLCs, government departments, international bodies and United Nations agencies, etc.",
        },
        {
            "type": "prose",
            "heading": "Tip - Alumni search",
            "variant": "callout-tip",
            "body": "Have a look at the 'Alumni' section of both UQ and your high school (where applicable). In this section, you can search for people by title, keyword or company. Where you limit your search to 'legal', do some further digging to see if someone from your high school or from UQ is doing a legal job that aligns with your career aspirations, whether that be because of the organisation they work at, the achievements they've made in their career, or particular attributes about them that you identify with. From there, send an invitation with a drafted message showing your interest as a law student in following that part of their career, referencing that common element of education. Give it a try! If they respond and connect with you, you might even want to schedule an information interview either in person or on video call to hear about their experience and better understand what's right for you in building your career.",
        },
    ],
    "relatedResources": ["information-interview-guide", "personal-branding-and-networking-tips"],
})


# B3.4 Information Interview Guide
write("information-interview-guide", {
    "slug": "information-interview-guide",
    "category": "jatl-career-tips",
    "title": "Information Interview Guide",
    "status": "published",
    "byJatl": True,
    "intro": "*Information Interview Outreach - LinkedIn & Email Templates*",
    "sections": [
        {
            "type": "prose",
            "heading": "What is an information interview?",
            "body": "An information interview is a short, informal conversation where you ask a legal practitioner about their career path, practice area, or workplace. The goal is insight and relationship-building - not securing a job. Approaching it this way makes practitioners far more willing to say yes.",
        },
        {
            "type": "comparison",
            "heading": "Which channel should I use?",
            "columns": [
                {"label": "LinkedIn message", "items": ["You found them through LinkedIn", "No direct email address available", "They are active on the platform", "Warmer, more conversational tone preferred"]},
                {"label": "Email", "items": ["You have their work email address", "You were referred by a mutual contact", "Contacting a senior or formal practitioner", "A structured, formal approach is preferred"]},
            ],
        },
        {
            "type": "prose",
            "heading": "LinkedIn message templates",
            "subheading": "Before you send - LinkedIn checklist",
            "body": "- Connect first with a personalised note, or message directly if you share a connection\n- Review their full profile thoroughly - reference something specific in your note\n- Keep the connection request note under 300 characters\n- Do not attach your resume or ask for a job at this stage\n- Wait 1 to 2 days after connecting before sending the main message",
        },
        {
            "type": "template",
            "heading": "Step 1 - Connection request note",
            "intro": "This note has one job: get the connection accepted. Keep it short, specific, and low-pressure. Save the interview request for the follow-up message.",
            "meta": "~300 characters max",
            "copyButton": True,
            "body": "Hi *[First name]*, I'm a *[e.g. third-year]* law student at UQ with a strong interest in *[practice area]*. I came across your profile and was genuinely impressed by your work in *[specific area, matter, or article]*. I'd love to connect - no agenda, just keen to learn from people working in this space.",
        },
        {
            "type": "template",
            "heading": "Step 2 - Follow-up message (after connecting)",
            "intro": "Send this message 1 to 2 days after they accept your connection. A separate message feels less transactional than bundling the request into the connection note.",
            "copyButton": True,
            "body": "Hi *[First name]*, thanks for connecting - I really appreciate it. I'm reaching out because I'm genuinely interested in *[practice area / career path]*, and your experience at *[firm or organisation]* - particularly *[specific aspect of their work]* - really stood out to me. I'd love to ask you a few questions about your path into this area, if you'd be open to it. I'm thinking a 20 to 30 minute call or video chat at a time that suits you - I'm not looking for a job, just hoping to learn from someone doing work I find genuinely interesting. Completely understand if your schedule doesn't allow for it. Either way, thanks so much for connecting.\n\n*[Your full name]*\n*[UQ Law, Year X]*",
        },
        {
            "type": "template",
            "heading": "If they seem hesitant or decline",
            "copyButton": True,
            "body": "Hi *[First name]*, no pressure at all - I completely understand how busy things get. If it's ever easier, I'm also happy to send a couple of questions over message if that's more convenient. Thanks again for connecting.",
        },
        {
            "type": "prose",
            "heading": "Email templates",
            "subheading": "Before you send - email checklist",
            "body": "- Verify the email address carefully - check the firm website for the correct format\n- Write a subject line that is clear and professional, not vague or clickbait\n- Name-drop a mutual connection in the opening line if you have one\n- Keep the email to four short paragraphs - brevity signals respect for their time\n- Send from your UQ student email address (e.g. your.name@uq.net.au)\n- Do not attach anything unless specifically requested",
        },
        {
            "type": "template",
            "heading": "Main outreach email",
            "subjectLine": "UQ law student - request for a brief conversation",
            "copyButton": True,
            "body": "Dear *[Mr / Ms / Dr Surname]*,\n\n*[Optional - if referred: I was encouraged to reach out by [Name], who spoke very highly of your work in [area].]*\n\nMy name is *[Your Full Name]*, and I am a *[year]*-year law student at the University of Queensland, where I am focusing on *[relevant area of study or interest]*. I have been following your work with interest - particularly *[specific matter, publication, case, or initiative]* - and would very much appreciate the opportunity to hear your perspective on *[specific topic, e.g. building a practice in this area / the realities of commercial litigation]*.\n\nI am writing to ask whether you might be willing to spare 20 to 30 minutes for a brief conversation, whether in person, by phone, or via video call. I am not seeking employment; I am simply hoping to learn from someone with real experience in a field I care about.\n\nI recognise you are very busy, and I am grateful for your time regardless of your answer. If you are open to it, I am happy to work around your schedule entirely.\n\nWarm regards,\n*[Your Full Name]*\n*[Year]* LLB/JD Student, The University of Queensland\n*[Phone number]*\n*[LinkedIn profile URL]*",
        },
        {
            "type": "prose",
            "heading": "Subject line variations",
            "body": "- **Default:** \"UQ law student - request for a brief conversation\"\n- **If referred:** \"Introduction from [Mutual contact] - brief conversation request\"\n- **Following up on specific work:** \"Your [article/achievement] on [X] - a question from a UQ law student\"",
        },
        {
            "type": "template",
            "heading": "Follow-up email (if no reply after 7 to 10 days)",
            "intro": "Send only one follow-up. If there is still no reply after that, move on gracefully. Persistence beyond one follow-up risks leaving a negative impression.",
            "subjectLine": "Re: UQ law student - request for a brief conversation",
            "copyButton": True,
            "body": "Dear *[Mr / Ms / Dr Surname]*,\n\nI hope this finds you well. I wanted to follow up briefly on my earlier email in case it got lost in a busy inbox. I would still love the chance to speak with you if your schedule allows - even a 15-minute call would be enormously valuable.\n\nIf now isn't a good time, I completely understand. Thank you again for your consideration.\n\nWarm regards,\n*[Your Full Name]*",
        },
        {
            "type": "comparison",
            "heading": "Tone - dos and don'ts",
            "columns": [
                {"label": "Do", "items": ["Be specific about why you chose this person", "Show you have researched their work", "Make the ask low-pressure and time-bound", "Use your UQ student email for formal emails", "Follow up once only if there is no reply"]},
                {"label": "Don't", "items": ["Ask for a job or internship in the first message", "Send the same generic message to everyone", "Follow up more than once", "Attach your resume unless specifically asked", "Use informal language or abbreviations"]},
            ],
        },
        {
            "type": "prose",
            "heading": "After they say yes",
            "body": "- Reply promptly to confirm the time and thank them warmly\n- Prepare 4 to 5 thoughtful questions in advance - research their recent work beforehand\n- Arrive on time and be concise - respect the time limit you proposed\n- Send a brief, personalised thank-you message within 24 hours of the conversation\n- Stay in occasional touch - share a relevant article, or update them when you land a clerkship\n\n*Building a genuine ongoing relationship is the long-term goal. The information interview is the first step, not a one-off transaction.*",
        },
        {
            "type": "prose",
            "heading": "You've Got This!",
            "variant": "callout-tip",
            "body": "Treat each outreach as a small experiment - some will land, others won't, and the only failure is not trying. Be kind to yourself and keep going.",
        },
    ],
    "relatedResources": ["linkedin", "personal-branding-and-networking-tips"],
})


# B3.5 JATL Recommends (partial)
write("jatl-recommends", {
    "slug": "jatl-recommends",
    "category": "jatl-career-tips",
    "title": "JATL Recommends",
    "status": "partial",
    "byJatl": True,
    "intro": "*This page is a work in progress. Content marked below is being finalised.*",
    "sections": [
        {
            "type": "prose",
            "heading": "UQ Pro Bono Centre",
            "body": "*(Intro paragraph coming soon.)*\n\n**Join the UQ Pro Bono Centre**\n\n- *(How to join - content pending.)*\n- *(How to get onto the service roster email - content pending.)*",
        },
        {
            "type": "prose",
            "heading": "Organisations for Young Queensland Lawyers",
            "body": "*(Intro paragraph coming soon.)*\n\n- **Queensland Young Lawyers** - description pending.\n- **The Legal Forecast** - description pending.",
        },
    ],
    "relatedPathways": ["community-legal-centres"],
})

print("All resource JSON files generated.")
