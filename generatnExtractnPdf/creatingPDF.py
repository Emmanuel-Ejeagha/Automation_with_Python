# This script creates a pdf file
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('generatnExtractnPdf/img.png', w=80, h=50)
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='ALX GRADUATION', align='C', border=1, ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description:', ln=1)

pdf.set_font(family='Times', size=12)
txt0 = """
ALX is a leading tech training provider that focuses on equipping individuals with the skills and knowledge necessary for careers in software engineering, data science, and other high-demand fields. It is part of the African Leadership Group, an organization dedicated to transforming Africa by developing the next generation of leaders. ALX offers rigorous, market-driven programs designed to address Africa's talent gap and create job opportunities in the tech industry.

Key Aspects of ALX:
Tech Programs: ALX offers intensive programs in areas such as software engineering, data science, cloud computing, and more. These programs typically last several months and are designed to provide hands-on, real-world experience.

Collaborations: ALX collaborates with industry leaders like Holberton School and AWS to ensure its curriculum is up-to-date and aligned with industry demands. These partnerships provide learners with high-quality resources, mentors, and opportunities for job placements.

Focus on Africa: ALX primarily focuses on addressing Africa's unemployment crisis by empowering young people with digital skills. However, its programs are also available to learners globally. The goal is to bridge the talent gap between Africa and the global tech industry.

Holberton Partnership: ALX Software Engineering program is built on the curriculum of Holberton School, which is known for its project-based and peer-to-peer learning approach. The program focuses on foundational and advanced topics in software development, including algorithms, data structures, APIs, and more.

Career Development: ALX is deeply committed to helping its students land jobs. In addition to technical training, the programs include soft skills development, interview preparation, and networking opportunities with potential employers.

Community and Mentorship: ALX fosters a strong learning community, with peer support and mentorship playing key roles in student success. Students are encouraged to collaborate on projects, which helps them build not only technical expertise but also teamwork and communication skills.

#100DaysOfCode Challenge: Many ALX students participate in coding challenges like the #100DaysOfCode initiative, where they commit to learning and coding every day for 100 days. This helps learners stay consistent, document their progress, and build an online presence.

ALX aims to create a sustainable talent pipeline by training individuals to meet the growing demand for tech professionals across Africa and beyond.
"""

pdf.multi_cell(w=0, h=15, txt=txt0)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=200, h=15, txt='PROGRAMS')

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=15, txt='DURATION', ln=1)

pdf.set_font(family='Times', size=14)
pdf.cell(w=200, h=15, txt='ALX SE')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=15, txt='12 months', ln=1)

pdf.output('generatnExtractnPdf/output.pdf')