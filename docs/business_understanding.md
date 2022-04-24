# Business understanding

## **Determine business objectives**

---

### **Background**

Most modern companies rely on machine learning solutions to increase their competitiveness and consolidate or improve their position in the market.  Companies that offer entertainment services like no other are focused on recommendations that satisfy each client. The company must find a way to satisfy that condition. A recommendation system was chosen as the proposed solution. 

### **Business objectives**

The primary objective of the company is to consolidate or even improve their share in global entertainment market. To do we should offer a personalized service for each client to increase their loyalty to the service.  

### **Business success criteria**

The project and integration with the service will be judged by increase in spent time of the customers per visit and customer satisfaction over the service.

## **Assess situation**

---

### **Inventory of resources**

The personnel available for the project is constrained by 5 people team: 1 business analyst, 1 project manager, 1 data scientist, 1 machine learning engineer, 1 business unit manager. The data available for the project is any fixed extracts of open-source data which relate to the purpose of the project and any data received through scrapping of related websites with open-source APIs. Computing resources is restricted to use of **???**.  In terms of software usage, Github was chosen as base version control system, as the main team-management software Notion was chosen, PowerPoint and Tableau were chosen as means for preparation of report and presentation of the project.

### **Requirements, assumptions and constraints**

The project is required to be finished by 15th of May and each step of researching and development should be well documented and organized. The results of the project should be indicative for the service, taking into account that the quality of the data may affect them, as well as data should be nonproprietary. For success of the project team should assume that there are no change in behaviour among clients and their do not provide self-contradictory feedbacks. The project is mostly constrained by time of completion, small personnel and limited computing resources.

### **Risks and contingencies**

Despite all precautions, risks for the project are still exist. One of the main risks is poor data quality which may lead to non-comprehensive analysis of the customers behaviour and misleading result of the project. The customer attrition for reasons uncontrolled by the company may lead to decrease in revenue and to the uselessness of this project. The major risk for the project is a drasticall change in customers behaviour to which recommender system developed within project will not be able to adapt. 

### **Terminology**

The glossary of terminology relevant to the project is consist from to main parts - business terminology and data mining terminology. 

**Business terminology:**

- Clientele loyalty - customer's likeliness to do repeat business with our company
- Results indicative for the service - results which may be useful for increasing market share and clientele loyalty
- Personalized service - providing customer experiences that are tailored to the consumer's individual needs and preferences

**Data mining terminology:**

- API - application program interface, which provides a means by which programs written outside of the system can interface with the system to perform additional functions.
- Accuracy - accuracy refers to the rate of correct values in the data
- Ground truth - information that is known to be true, provided by direct observation and measure
- Test data - dataset independent of the training dataset, used to compare the estimates of the model with ground truth results

### **Costs and benefits**

**Costs:** indirect costs(electricity and etc.); intangible costs(customer's behaviour)

**Benefits:** Higher revenue and sales; increase in customer satisfactions; structuring processes and space within the company

## **Determine data mining goals**

---

### **Data mining goals**

Use historical information about previous views to generate a model that links “related” movies. When users look at a movie description, provide links to other movies in the related group (market basket analysis).

### **Data mining success criteria**

The project will be considered as a successful in terms of data mining goals if 70% accuracy of recommendations will be reached on the test data.

## **Produce project plan**

---

### **Project plan**

1. Business understanding:
    - determine business requirements, evaluate a possible solutions and the strategies for achieving goals
    - take into account costs and benefits for future assessment
2. Data understanding
    - describe data
    - find first insights to the data
    - assess data quality and applicability to the goal achievement
3. Data preparation
    - clean data
    - format data for the modeling step
    - add additional insights from data to modeling step
4. Modeling
    - select modeling based on the data
    - generate test and assess model's quality
5. Evaluation
    - evaluate the model in terms of correctness and applicability
6. Deployment
    - deploy the solution for the goal
    - collect the new data based on the solution and return to the evaluation step to assess the quality of solution by A/B test

### **Initial assessment of tools and techniques**

As the main tool for prototyping and development the programming language Python was chosen; team management is performed with use of Notion.