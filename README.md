
IEEE 830-1998 Software Requirements Specification

## TITLE: "Translate-o-Rama: Get Your Texts Translated in a Jiffy!"

# Table of Contents

1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
   1. [Product Perspective](#21-product-perspective)
   2. [Product Functions](#22-product-functions)
   3. [User Classes and Characteristics](#23-user-classes-and-characteristics)
   4. [Operating Environment](#24-operating-environment)
   5. [Design and Implementation Constraints](#25-design-and-implementation-constraints)
   6. [User Documentation](#26-user-documentation)
   7. [Assumptions and Dependencies](#27-assumptions-and-dependencies)
3. [Specific Requirements](#3-specific-requirements)
   1. [Functional Requirements](#31-functional-requirements)
      1. [User Requirements](#311-user-requirements)
      2. [Translator Requirements](#312-translator-requirements)
      3. [Admin Requirements](#313-admin-requirements)
4. [System Interfaces](#4-system-interfaces)
   1. [User Interfaces](#41-user-interfaces)
   2. [Hardware Interfaces](#42-hardware-interfaces)
   3. [Software Interfaces](#43-software-interfaces)
5. [Other Nonfunctional Requirements](#5-other-nonfunctional-requirements)
6. [Other Requirements](#6-other-requirements)

## 1. Introduction

### 1.1 Purpose 

The purpose of this document is to provide a Software Requirements
Specification (SRS) for the development of “Translate-o-Rama”, a web
application that enables users to hire translators to translate their texts
quickly and conveniently. This document describes the requirements of the web
application from the perspectives of the user, system, and customer. 

### 1.2 Document Conventions

This document is written using the IEEE 830-1998 standard for software
requirements specifications. It will include user, system, and customer
requirements for the completion of the project. 

### 1.3 Intended Audience and Reading Suggestions

This document is intended for the developers and designers working on the
"Translate-o-Rama" project. It's recommended that readers start from the
beginning and read the document from start to finish to get a complete picture
of the project requirements. 

### 1.4 Product Scope

The scope of "Translate-o-Rama" is to create a web application that allows
users to post translation jobs with ease, helps customers find the right
translator for their job, and enables translators to submit quotes and view
available jobs. It will also provide an easy and secure payment experience, and
an orderly review system.

### 1.5 References 

1. IEEE 830-1998: IEEE Standard for Software Requirements Specifications (IEEE,
   1998).
2. Django 4.1. documentation

### 1.6 Overview

The "Translate-o-Rama" web application will be a platform for users to post
translation jobs and for translators to submit quotes. The application will
also provide a secure payment system and a review system for users to rate
their experience with translators.

The sections of this document are as follows:
- Section 2: Overall Description


## 2. Overall Description

### 2.1 Product Perspective

Translate-o-Rama is a web application designed to help users find the perfect
translator for their project, quickly and easily.

The user interface is designed to be intuitive and easy to use, with an Admin
dashboard, User dashboard, and a public part with a list of translators and a
list of available jobs filterable by language and field. Users can click on a
particular Translator's profile and view their previous translations and
reviews. There is also an in-app messaging system for users to communicate with
translators.

Users can post jobs and receive quote requests from translators, as well as
view the estimated cost of their translation project.  Translations are
delivered through the app. Users are notified when the job is complete, and the
payment is handled using a cryptocurrency token. If there is a dispute or
disagreement between users and translators, an admin user will review the case
and make a decision.

Translate-o-Rama also offers a rating system for translators, as well as a
searchable database of translators so users can easily find the perfect
translator for their project. All translators must submit their credentials,
such as diplomas, which will be approved by an admin user. Unfortunately, there
is no automated quality assurance process.

With Translate-o-Rama, users will be able to quickly and easily find the
perfect translator for their project.

Translate-o-Rama is a self-contained web application that will be hosted on a
web server. It will be accessible through a web browser.


  
### 2.2 Product Functions

"Translate-o-Rama" will provide the following functions:

- User Interface: Users will be able to navigate between pages on the web 
 application, communicate with translators, view the names of the 
 translators working on their projects, contact a translator before 
 assigning a project, and view the estimated cost of their translation 
 projects.

- Job Posting and Assignment: Users will be able to post jobs and receive 
 quotes from translators, delete the jobs, 
 and request a specific translator for their translation project.

- Job Delivery and Payment: Users will be notified when their translations 
 are complete, and the web application will handle the delivery of 
 completed translations, disputes or disagreements between users and 
 translators, payments, and invoicing.

- Review System: The web application will include a rating system for 
 translators, as well as allow users to review the quality of their 
 translations.

- Job and Translator Search: The web application will provide a searchable 
 database of translators, and will verify the credentials and 
 qualifications of translators.


### 2.3 User Classes and Characteristics

The product will have three logical user classes: Admin, User, and Translator.
However, the web application will only have two user classes implemented: Admin and User.
Admin is a user class with a superuser status, and can access the Admin
dashboard. Admin users can create, edit, and delete users.

Each user can be both a User and a Translator. Every user can both post jobs 
and submit quotes. 


#### 2.3.1 Admin

Admin users will be able to manage the web application, including managing
users, managing translators, and managing jobs. Admin users will also be able
to review disputes and disagreements between users and translators. Since the app
wil use a cryptocurrency token, admin users will be able to manage the token
allocation to users and translators. 

#### 2.3.2 User

Users will be able to post jobs, assign jobs to translators, and view the
status of their jobs. Users will also be able to review the quality of their
translations.

#### 2.3.3 Translator

Translators will be able to view available jobs, submit quotes, and view the
status of their jobs. 

### 2.4 Operating Environment

The web application will be hosted on a web server. It will be accessible
through a web browser. 

### 2.5 Design and Implementation Constraints

The web application will be written in Python using the Django framework. It
will be hosted on a web server. The data will be stored in a SQLite database.
No further design and implementation constraints are known at this time.

### 2.6 User Documentation

No documentation will be provided to users.

### 2.7 Assumptions and Dependencies

The application will use a cryptocurrency token to handle payments. For the
first version of the application, the amounts of tokens each user have will be
recorded as a field in the database and will be managed by admin users. The token
deposit and withdrawal funtionality will not be implemented in this version of
the application.

The application will not have an automated quality assurance process.



## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Requirements

##### 3.1.1.1 User Registration

**Req U1** - The web application will allow users to register for an account.

The web application will allow users to register for an account. Users will
provide their name, email address, and password. The web application will
verify that the email address is unique and not already used by another user.

##### 3.1.1.2 User Login

**Req U2** - The web application will allow users to log in to their account.

The web application will allow users to log in to their account. Users will
provide their email address and password. The web application will verify that
the email address and password match the information in the database.

##### 3.1.1.3 User Logout

**Req U3** - The web application will allow users to log out of their account.

The web application will allow users to log out of their account. Users will
click on a "Log Out" button in the Navigation. The web application will
terminate the user's session.

##### 3.1.1.4 User Dashboard

**Req U4** - The web application will provide a dashboard for users to view
their account information and manage their jobs.

The web application will provide a dashboard for users to view their account
information and manage their jobs. The dashboard will include the following
information:

- User's name
- User's email address
- User's token balance
- List of jobs posted by the user
- A list of quotes for jobs posted by the user
- A link to the translator's profile for each quote
- A link to the translator's profile for each accepted job
- Messages from other user ordered by date from newest to oldest

##### 3.1.1.5 User Profile

**Req U5** - The web application will provide a profile for users to view
and edit their account information.

The web application will provide a profile for users to view and edit their 
account information. The profile will include the following information:

- User's name
- User's email address
- User's accepted jobs
- User's completed jobs

The user will be able to change their email address or their password on this 
page.

##### 3.1.1.6 Job Posting

**Req U6** - The web application will allow users to post jobs.

The web application will allow users to post jobs. Users will provide the
following information:

- Job title
- Job description
- Job source language
- Job target language
- Job field
- Job budget
- The text to be translated

The web application will verify that the job title is unique and not already
used by another job. The web application will verify that the job source
language and job target language are different. The web application will verify
that the job budget is a positive number. The web application will verify that
the job field is one of the following: "Art", "Business", "Computers", "Education",
"Engineering", "Finance", "Law", "Literature", "Medicine", "Science", "Social
Sciences", or "Technology".

##### 3.1.1.7 Job Assignment

**Req U7** - The web application will allow users to accept a quote from a
translator and assign a job to the translator.

The web application will allow users to accept a quote from a translator and
assign a job to the translator. Users will click on a "Accept" button next to
the quote. The web application will assign the job to the translator and notify
the translator that the job has been assigned to them.

##### 3.1.1.8 Job Status

**Req U8** - The web application will allow users to view the status of their
jobs.

The web application will allow users to view the status of their jobs. Users
will click on a "View Status" button next to the job. The web application will
display the status of the job.

##### 3.1.1.9 Job Delivery

**Req U9** - The web application will allow users to view the completed
translation of their jobs.

The web application will allow users to view the completed translation of their
jobs. Users will click on a "View Translation" button next to the job. The web
application will display the completed translation of the job.

##### 3.1.1.10 Job Review

**Req U10** - The web application will allow users to review the quality of
their translations.

The web application will allow users to review the quality of their
translations. Users will click on a "Review" button next to the job. The web
application will display a form for the user to provide a review. The web
application will verify that the review is between 1 and 5 stars.

After the user submits the review, the web application will update the
translator's rating. The web application will calculate the new rating by
calculating the average of all the reviews for the translator. The web
application will update the translator's rating in the database. The web 
application will transfer the tokens for the job from the users balance to the 
translators balance.


##### 3.1.1.11 User Messaging

**Req U11** - The web application will allow users to send messages to
other users.

The web application will allow users to send messages to other users. Users
will click on a "Message" button next to the job. The web application will
display a form for the user to provide a message. The web application will
verify that the message is not empty.

After the user submits the message, the web application will send the message
to the other user. The web application will display the message on the user's
dashboard.


##### 3.1.1.12 Job listing

**Req U12** - The web application will allow users to view a list of jobs
posted by other users. 

The web application will allow users to view a list of jobs posted by other
users. Users will click on a "Jobs" button in the Navigation. The web
application will display a list of jobs posted by other users. The list will
only show unassigned jobs. The list will include the following information:

- Job title
- Job description
- Job source language
- Job target language
- Job field
- Job budget
- A link to the user's profile
- A "Bid on Job" button
- A "Message User" button 


##### 3.1.1.13 Job Dispute 

**Req U13** - The web application will allow users to dispute a job.

The web application will allow users to dispute a job. Users will click on a
"Dispute" button next to a completed job. The web application will display a form for
the user to provide a dispute. The web application will verify that the dispute
is not empty.

The dispute will be handled by the administrator manually. The dispute has to
contain the following information:

- Details about the job
- The user that posted the job
- The user that completed the job
- The reason for the dispute (provided by the user that posted the job)





#### 3.1.2 Translator Requirements

Translator requirements focus on the specific funtionalities that Users that wish 
to translate jobs will be able to use. 

Translators use the same registration and login process as users. The only difference
is that during the registration process, users will be able to click a checkbox stating
that they also wish to be a translator. 

User interface options intented for the translators will be visible only to users that
selected the option to be a translator during the registration process.

General user interface options and functions will be visible to all users,
including the translators.

##### 3.1.2.1 Choose to be a Translator

**Req T1** - The web application will allow translators to register as a
translator.

The web application will allow translators to register as a translator. During
the registration process, translators will be able to click a checkbox stating
that they also wish to be a translator.

##### 3.1.2.2 Translator Dashboard

**Req T2** - The web application will provide a dashboard for translators to
view their account information.

The web application will provide a dashboard for translators to view their
account information. The dashboard for translators will be the same one for the
users described in **Req U4**. The only difference is that the dashboard for
translators will include the following information:

- A list of submitted bids
- A list of assigned jobs
- A list of completed jobs
- Translators's rating


##### 3.1.2.3 Translator Profile

**Req T3** - The web application will provide a profile for translators to
view their account information.

The web application will provide a profile for translators to view their
account information. The profile for translators will be the same one for the
users described in **Req U5**. The only difference is that the profile for 
translators will include the following information:

- A list of submitted bids
- A list of assigned jobs
- A list of completed jobs
- Translators's rating


##### 3.1.2.4 Job Bidding

**Req T4** - The web application will allow users to bid on jobs posted by
other users.

The web application will allow users to bid on jobs posted by other users. The
jobs will be listed in the same way as described in **Req U12**. Users will
click on a "Bid on Job" button next to the job. The web application will
display a form for the user to provide a quote. The web application will verify
that the quote is a positive number.

After the user submits the quote, the web application will send the quote to
the user who posted the job. The web application will display the quote on the
user's dashboard.


##### 3.1.2.5 Job Status

**Req T5** - The web application will allow translators to view the
status of their jobs.

The web application will allow translators to view the status of their
jobs. The possible statuses are: "Assigned", "In Progress", "Completed".
The web application will display the status of the job.


##### 3.1.2.6. Job Delivery

**Req T6** - The web application will allow translators to complete the
translation of their jobs.

The web application will allow translators to complete the translation
of their jobs. Translators will click on a "Complete" button next to the job.
The web application will display a form for the translator to provide the
completed translation. The web application will verify that the translation is
not empty.

After the translator submits the translation, the web application will send the
translation to the user who posted the job. The web application will display
the translation on the translator's dashboard.


#### 3.1.3 Admin Requirements

Admin requirements focus on the specific funtionalities that Admins will be able
to use. Admins are created by the system administrator in the Admin Dashboard.
The Admins use the Django Admin interface to manage the system.

##### 3.1.3.1 Admin Dashboard

**Req A1** - The web application will provide a dashboard for admins to
manage the system. 

The web application will provide a dashboard for admins to manage the system.
The dashboard will use the Django Admin interface. The dashboard will allow
admins to manage the following:

- Users (create, edit, delete)
- Jobs (create, edit, delete)
- Apply a token balance to a user


##### 3.1.3.2. Apply a Token Balance to a User

**Req A2** - The web application will allow admins to apply a token balance
to a user.

The web application will allow admins to apply a token balance to a user. The
web application will allow the admins to find a user in the Admin dashboard and 
to change the user's token balance. The web application will update the user's
token balance in the database. The web application will display the new token
balance on the user's dashboard.

**Constrainst and considerations:**
The token balance is used for payments in the system. The token balance is
applied to the user's account when the user completes a job. The token balance
is deducted from the user's account when the user posts a job. 
The deposit and withdrawal of the tokens is outside the scope of this application.

The admins will verify the user's deposit outside of the application and will
apply the token balance to the user's account in the application. Likewise, the
admins will process the user's withdrawal requests outside of the application and
will deduct the token balance from the user's account in the application.

In this way, the application will not be responsible for the communication
between the users and the admins. All the communication between the users and
the admins regarding the token balances will be done outside of the
application. The admins will then apply the token balance to the user's account
through the Admin dashboard.

**Note:** The token balance is not a currency (yet). The token balance is a number
that represents the number of tokens that the user has in their account. The
token balance is used for payments in the system.


##### 3.1.3.3 Dispute Resolution

**Req A3** - The web application will allow admins to resolve disputes.

The web application will allow admins to resolve disputes. The web application
will allow the admins to find a dispute in the Admin dashboard and to resolve
the dispute. The dispute will be resolved by the admin manually. The admin will 
contact the job poster outside the application and will resolve the dispute
manually.  All the changes to the users' ratings or token balances will
be done manually by the admin from the Admin dashboard.

Once the dispute is resolved, the admin will close the dispute. The admin will
close the dispute by changing the status of the dispute to "Closed" in the
Admin dashboard. The web application will display the status of the dispute as
"Closed" on the user's dashboard.



### 3.2 Usability Requirements

The web application will be designed to be easy to use. The web application will
be designed to be intuitive and easy to learn. 



### 3.3 Reliability Requirements

None a this time

### 3.4 Performance Requirements

None a this time

### 3.5 Supportability Requirements

None a this time

### 3.6 Design Constraints

None a this time

## 4. System Interfaces

### 4.1 User Interfaces

The application will have a user interface that is accessible via a web
browser. The interface will be designed to be intuitive and user-friendly,
optimized for mobile and desktop devices.


The web application will use a standard web interface with a top navigation bar
and a main content area. The web application will be primarily used on a
desktop computer and a responsive design is not required.

The top navigation bar will have the following links:

* On the left side:
  - Logo (link to the home page)
  - Jobs (a link to the Job listing page)
  - Post a Job (a link to the Post a Job page)

* On the right side:
  - Login (a link to the Login page) if the user is not logged in
  - Profile (a link to the Profile page) if the user is logged in
  - Logout (a link to the Logout page) if the user is logged in
  - My Jobs (a link to the My Jobs page) if the user is logged in



### 4.2 Hardware Interfaces
The application will be hosted on a secure web server running on Linux or Windows.

### 4.3 Software Interfaces
The application will use Django 4.0, the database will be SQLite, frontend framework will be Bootstrap.

### 4.4 Communications Interfaces
The application will have a secure communication interface for secure data transfer.

## 5. Other Nonfunctional Requirements

### 5.1 Security Requirements
The application will use the Django's default User management system. The
application will use Django's default authentication system. The application
will use Django's default authorization system. The application will use Django's
default password reset system.

### 5.2 Safety Requirements
The application must be designed to prevent the user from performing any unsafe actions or operations.

### 5.3 Business Rules
The application will have business rules in place to ensure the safety and security of user data.

### 5.4 Quality Attributes
The application must have a high quality user interface with good usability and responsiveness. The application must also have an uptime of at least 99.

## 6. Other Requirements

### 6.1 Business Requirements

None a this time

### 6.2 Regulatory Requirements

None a this time
