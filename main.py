import streamlit as st
import datetime


#General Settings
page_title = "Resume | Kanishkar K"
page_icon = ':wave:'
name = "Kanishkar K"
job_title = "Software Engineer"
location = "India"
contact = [
    {
        "channel": "kanishkar51015@gmail.com",
        "icon": "https://img.icons8.com/?size=18&id=86840&format=png&color=000000",
        "link": "https://kanishkar51015@gmail.com"
    },
    {
        "channel": "kkanishkar",
        "icon": "https://img.icons8.com/?size=20&id=xuvGCOXi8Wyg&format=png&color=000000",
        "link": "https://www.linkedin.com/in/kkanishkar/"
    },
    {
        "channel": "kanishkar51015",
        "icon": "https://img.icons8.com/?size=20&id=62856&format=png&color=000000",
        "link": "https://github.com/kanishkar51015"
    }
]

profile = "Enthusiastic problem solver with over 2 years of experience in delivering reliable technical solutions. A highly empathetic team player, driven by a desire to learn and grow, and dedicated to shaping a brighter future."
skills = {
    "Programing languages": ["JavaScript", "TypeScript", "Python", "C", "C++", "Sql"],
    "Full-stack": ["HTML", "CSS", "ReactJS", "VueJS", "NodeJS", "Django","Postgres", "MongoDB", "Docker" ],
    "AI and ML": [ "Scikitlearn", "NumPy", "Pandas", "Langchain", "TensorFlow"],
    "Low-code Tools": ["Retool", "N8N", "Zapier", "AppScript"]
}
expirence = [
    {
        "role": "Software Engineer",
        "company": "Nova Benefits",
        "from": "2022-05-17",
        "to": "Present",
        "description": "Worked closely with clients and internal teams to understand their needs, quickly developed and implemented custom tools and integrations, and documented the solutions for future reference. Continuously maintained and improved tools based on user feedback.",
        "projects": [
            "Developed Generative AI-powered tools integrated with email, slack, whatsApp, and google meet to generate summaries, feedback, and validation scores, enhancing executive performance.",
            "Created an internal tool for insurance and financial data processing, including sanity checks and business calculations, cutting processing time by 5 days.",
            "Designed workflows for delivering timely client updates via WhatsApp and email channels, increasing client engagement by 10%.",
            "Implemented customised onboarding flows tailored to client needs, leading to a 5% increase in retention and a competitive edge.",
            "Created analytics dashboards and automations by integrating databases, Zoho (ERP), and lead source forms to enhance team performance.",
            "Developed multiple python automation and data scraping scripts to streamline processes for the supply team."
        ],
        "link": "https://www.novabenefits.com"
    },
    {
        "role": "Retool Consultant",
        "company": "Foundation AI",
        "from": "2024-02-01",
        "to": "2024-07-21",
        "description": "Designed and implemented a network of internal tools in Retool, seamlessly integrating PostgreSQL, AWS S3, and Salesforce to enhance customer management and streamline file processing. And also Mentored a team of 3 engineers on NodeJS, ReactJS and internal tools development.",
        "projects": [],
        "link": "https://www.foundationai.com"
    },
    {
        "role": "Data Engineer Intern",
        "company": "Cognizant",
        "from": "2022-02-01",
        "to": "2022-04-30",
        "description": "Received training in OOPs, Python, RDBMS, AWS and Google Cloud Platform along with soft skills like corporate culture integration, effective communication, and activity tracking.",
        "projects": [],
        "link": "https://www.cognizant.com/in/en"
    }

]
education = [
    {
        "degree": "B.Tech Computer Science with Specialization in AI and ML",
        "college": "SRM University",
        "from": "2018-06-06",
        "to": "2022-05-05",
        "cgpa": "9.8"
    },

]
personal_projects = [
    {
        "name": "Geolocation Data Analysis",
        "description": "Developed a solution using K-Means Clustering to recommend optimal accommodations for immigrants moving to a city. The project involved classifying accommodation options based on preferences such as amenities, budget, and proximity to desired locations. Data for this analysis was sourced through the Foursquare API, making recommendations more accurate and relevant.",
        "stack": "",
        "link": "https://github.com/kanishkar51015/geolocational-data-analysis/blob/main/Notebook.ipynb"
    },
    {
        "name": "URL Shortener",
        "description": "Created an API service designed to transform long URLs into shorter, more manageable links. This service simplifies sharing and tracking by generating concise URLs. The API ensures efficient link handling and straightforward integration for users.",
        "stack": "",
        "link": ""
    },
    {
        "name": "Audio Sources Separator",
        "description": "Developed a neural network using the Librosa library to separate vocals from accompaniments in music tracks. The project aimed to enhance audio processing capabilities by isolating vocal elements from instrumental components, leveraging advanced machine learning techniques for improved audio analysis and manipulation.",
        "stack": "",
        "link": "https://colab.research.google.com/drive/1KPl-kBSMTMJcz0oxIskkIFJMBxcTTq3C?usp=sharing"
    },
    {
        "name": "Deeply Supervised Practical Implementation of Violence Detection from Videos for Maximising Performance",
        "description": "Published a paper on violence detection, focusing on classifying videos into categories such as arrest, assault, arson, and abuse. Utilizing 200 videos from news channels and social media, the study employed pre-trained deep neural networks to develop a low-complexity method for detecting violent actions.",
        "stack": "",
        "link": "https://www.techrxiv.org/doi/full/10.36227/techrxiv.20060975.v1"
    },
    {
        "name": "Wrist Wearable Health Band for COVID-19 Testing",
        "description": "Published a paper on using smartwatches and fitness bands for COVID-19 screening, integrating sensors such as pulse sensors, pulse oximeters, accelerometers, and temperature sensors. The study demonstrates how these wearables can provide real-time health monitoring and risk assessment, offering a more efficient and accurate alternative to traditional methods.",
        "stack": "",
        "link": "https://openaccesspub.org/jmid/article/1452"
    },

]
language = ["English", "Tamil"]


st.set_page_config(page_title = page_title, page_icon = page_icon,)

with open('./styles/main.css') as s:
    st.markdown(f"<style>{s.read()}</style>", unsafe_allow_html = True)



#Hero section
st.title(name)
st.write(job_title)

#profile section
st.write(profile)

cols = st.columns(len(contact))
for (i,v) in enumerate(contact):
    if v['channel'] != "Phone":
        cols[i].write(f"![]({v['icon']}) [{v['channel']}]({v['link']})")
    else:
        cols[i].write(v['link'])
        


#Skills section
st.write("#")
st.subheader("Skills", anchor=False)
st.write("---")
cols = st.columns(len(skills), gap = "medium")
for i, (k,v) in enumerate(skills.items()):
    if len(v):
        c = cols[i].container()
        c.markdown(f"**{k}**")
        c.write("- " + "\n- ".join(v))

#Expirence section
#st.write("#")
st.subheader("Experience", anchor=False)
st.write("---")
for (i,v) in enumerate(expirence):
    c = st.columns([2,1])
    c[0].write(f"**{v['role']}** | {v['company']}")
    fromDate = datetime.datetime.strptime(v['from'],"%Y-%m-%d")
    fromStr = f"{fromDate.strftime('%B')} {fromDate.strftime('%Y')}"

    if(v['to'] != "Present"):
        toDate = datetime.datetime.strptime(v['to'],"%Y-%m-%d")
        toStr = f"{toDate.strftime('%B')} {toDate.strftime('%Y')}"
    else:
        toStr = "Present"
        
    c[1].write(f"**{fromStr} - {toStr}**")

    st.write(f"{v['link']}")
    
    if(v['description'] != ""):
        st.write(f"{v['description']}")
    
    if(len(v['projects'])):
        st.markdown("**Key Projects:**")
        projectStr = "- " + "\n- ".join(v['projects'])
        st.write(f"{projectStr}")

    st.write("#")

#Education
st.subheader("Education", anchor=False)
st.write("---")

for (i,v) in enumerate(education):
    fromDate = datetime.datetime.strptime(v['from'],"%Y-%m-%d")
    fromStr = f"{fromDate.strftime('%B')} {fromDate.strftime('%Y')}"
    toDate = datetime.datetime.strptime(v['to'],"%Y-%m-%d")
    toStr = f"{toDate.strftime('%B')} {toDate.strftime('%Y')}"
    
    c = st.columns([2,1])
    c[0].write(f"**{v['degree']}**")
    c[1].write(f"**{fromStr} - {toStr}**")

    st.write(f"{v['college']} | **CGPA: {v['cgpa']}**")



#Projects section
st.subheader("Personal Works", anchor=False)
st.write("---")

for (i,v) in enumerate(personal_projects):
    if(v["link"]!=""):
        st.write(f"[{v['name']}]({v['link']})")
    else:
        st.write(f"**{v['name']}**")
    
    st.write(f"{v['description']}")
    st.write("\n\n\n")
    