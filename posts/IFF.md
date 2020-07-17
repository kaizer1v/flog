TODO

* Github vs AWS
* Map interactivity
  - html page
  - embed block survey into pages
  - 

-----

# 6th June Meeting Notes

- Database should be an RDBMS data structure (@Shivani - could you kindly share details of how IFF is maintaining their website on AWS? - This will help us define the right database tool)
- Trustee + Shivani maintains the IFF website
- Data points are at state level + district level (similar to @pvamsikrishna97 - please share the link here if you can)
- PDFs will be stored in IFF's personal server (currently google drive). The link to this file will be saved in database though
- Documents collected by IFF are collated by govt websites (already open)


## User Cases Discussed

- To view state level summary and drill down to district level
- Able to access PDF for a particular FRT project + media article
- 


## TODO (before next call)

- Usability testing of seva privacy website (@Anushka Jain - could you please reshare the link here?)
- Get AWS details from @Shivani
- Update & answer the questions in the PRD


----

## Personal learning goal


# Goal
Make citizens aware of the existing FRT (face recognition technologies) systems and their purpose.

# Brief

IFF has a bunch of data that shows the locations for FRT cameras and devices, along with it's intended purpose - to make people aware of how/when they are being tracked.


## Data Points

* Authority - where the FRT is installed Eg: Airports Authority of India
* Place     - Bangalore airport
* Purpose   - reason why it was installed / intent Eg: authentication of identity
* Tech    - who provided the technology + software / cameras etc.
...

and other related information



## Aim of the System

* Collate this information and making it public
* 

## User / Persona

* Media
* 

## What all can the data provide?

* Show all places where a particular vendor installed their software/technologies
* Show all systems installed after / during a date/time duration
* Regional information about a state / district


## Other features

* Explainer on FRT
* Case Studies about legal analysis
* Collaboration opportunities
* Private member's bill on FRT being drafted / details

# Questions

* 

# Links

- [Current data points of where FRTs are installed](https://docs.google.com/spreadsheets/d/1kjgdiNHZw_YtSnHsadB5AEnYZYUYkiS65HUiJWJREPQ/edit#gid=0)
- The sheet explaining the [column names](https://docs.google.com/spreadsheets/d/1AxegtFhCuLh5BZu4XrJlGdPTGgTtbPS2unvCRudjNvk/edit#gid=0)


---

## Design deliverables

* Basic
  - Colour Theme
  - Typography
    => Primary = Nato Sans, Helvetica, sans-serif
    => Secondary = Lora, Helvetica Neue, Serif

  - Information Architecture
    => Sitemap
    => Page names
    => 

* UX Stuff
  - Persona details
  - 

* Navigation
  - Text
  - Selection / Deselection

* Content
  - Home page content
  - Layout

* 


Things required from IFF

1. Intro Text
  - What is FRT
  - Why are you here
  - How will it affect you (as a citizen / user)

2. About
  - Brief about IFF
  - Brief about DataKind

3. Petition
  - ...



## Final Members | Roles (Discussion 26th)

* Srihari Pramod - 
* Vamsi Krishna - 
* Richa Goyat - Project manager
* Romit Jain - 

* Srivalya - help with backend
* Vivek - help with design


Logistics
* DataKind's repository on github
* Slack for communication
* Trello board for work org & progress
* Weekly Saturday/Sunday calls on catchup (include US timezone for Richa)


TODO / Focus points
* Database to be setup
  - Cost involved
  - MySQL
  - Amazon Web service


Timeline
* June - July: DB + Querying the db using python + Design UI + interactions (MVP 1)
* July - Aug: Altair + visualization
* Aug - Sept: Fill other pages (MVP 2)


Questions / TODO
- Weekly breakdown of tasks for months (by 6th - after discussing with team)
- Who's github?
- Database - where to host?
- MIT vs Creative Commons (CC-BY)
- Agenda for 1st call
- Find open source tool for website analytics (AWS | Google | ...)
- Send invite for 1st call to volunteers (Friday 29th post 8:00
- NDA to be shared with team



-----

# Possible Insights from the data

* Overall stats



# IA

- Home
- Submit FRT
- Petition
- Case Studies
- RTIs
- About


# Wireframes

Objective of the design

* Mobile first application
* 


Links / Resources
-----------------
- [% of mobile vs desktop users India](https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/india)
- List of [open source icons](https://feathericons.com/)



Questions
---------

* Does mobile first approach make sense?
* Does mobile first approach affect the backend?

----

Insights for 

1. Citizens

  * India has
    -> ____ in my city
      -> where?
    -> ____ in my state
      -> where?
    -> state-wise distribution

  * So what can I do about it?
    -> sign petition
    -> add FRT system




----


* Best way to send push notification when IFF adds a new record
* process of adding new FRT system to the database from the crowd sourced entry
  - data filter / validation when collecting data from crowd sourced
  - 

* petition sign -> IFF receives it -> IFF sends email <via blocksurvey>
* 

Card Design
-----------

1. Authority Name + Location
2. Facial Recognition Name
3. Status
4. Financial Outlay (Amount)
5. RTI Filed + Replies



Insights
--------

Comparison

* # of FRT systems near me (within 10 km radius)
* Max spending by govt (correlation with tax?)
* 


----

Meeting on 27th - IFF

* Districts / States could be from a public open data
* upload status more human friendly
* hide the ID column
* minimise 


---

`/`
  - FileHandler -> will fetch the index.html file


`/frt`
  - FunctionHandler -> returns JSON of all FRT info required for viz

`/frt/<state_name>`
  - FunctionHandler -> returns JSON for specific state

`/frt/national`
  - FunctionHandler -> returns JSON for all national level FRTs

`/about`
`/submit_frt`
  - FileHandler -> will return .html files for each containing content + form etc.


`/case_studies`
  - FileHandler -> will return html template files with content

`/case_studies/<id>`
  - FileHandler -> will return html template for specific case study with content

