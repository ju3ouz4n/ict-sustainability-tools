# Data dictionary

_(v1.2 - last update May 13th 2024)_

If either the name, the definition or the values of the field should be updated for v1.1, put :people_hugging: next to the title and add a comment to clarify your suggestions. If the consensus which was reached still stands leave **✅**

If the field is required it should have the tag [R] after its name. Despite not being required, filling all the other fields (with “TBQ: To Be Qualified” or “NA: Not Applicable”) is kindly requested.

## Tool name ([tool_name] [R])  **✅**

The tool must have a well identified name and not being just an item in the menu of a bigger tool (e.g. not the “sustainability check” option in a development tool)

## Organization ([organization] [R]) **✅**

The legal entity having the intellectual property of the tool. In case of share intellectual property between organizations, all of them can be listed (comma separated).

## Website ([website] [R]) **✅**

The tool must have a dedicated web page (landing page, github repo, etc.) describing its functionnalities, its licencing, etc. Required format is a URL.

## Sub-module ([sub_module]) **✅**

If a tool has multiple modules based on different models and/or data entry point, several lines can be inserted for the same tool. Both the fields “Tool name” and “Organization” must have exact same values between the different sub-modules.

## Environmental indicators ([environmental_indicators] [R]) **✅**

Which environmental indicators are provided by the tool:

* Final Energy consumption (usually in Joule or WattHour),
* Primary Energy consumption (usually in Joule),
* GWP: [Global Warming Potential](https://en.wikipedia.org/wiki/Global_warming_potential) aka the carbon footprint usually in CO2 equivalent,
* ADPf (MJ): Abiotic ressource Depletion Potential for fossil fuel usually in Antimony (Sb) equivalent,
* ADPe (Sbeq): Abiotic ressource Depletion Potential for element (minerals, etc.) usually in Antimony (Sb) equivalent
* Water Depletion: also called water footprint
* PEF: [Product Environmental Footprint](https://green-business.ec.europa.eu/environmental-footprint-methods_en) Score
* Not Applicable: usually this value will disqualify a tool (see “Status”) except for “Best Practices” type of assessment.

## Quick description ([quick_description] [R]) **✅**

Ideally it should be the description provided by the owner of the tool.

## Assessment type ([assessment_type]) **✅**

What is the main purpose of the tool:

* Best practices: assessing some functional units against industry best practices without any intention to measure or evaluate footprint.
* Evaluation: assessing some functional units using a model to estimate an environmental indicator
* Measure: collecting the value of an environmental indicator for some functional units
* TBQ: To be Qualified

## Main Perimeter ([main_perimeter]) and Other Perimeters ([other_perimeters])**✅**

What is the general scope covered by the tool. Several values are possible but one should be chosen as the primary one for visual classification purpose:

* Global / Information System
* Global / Digital Advertising
* Global / Digital Workplace (for example: Slack, O365, Google Suite, Mattermost, Framateam, etc.)
* Infra / Datacenter
* Infra / Cloud (for example: GCP, AWS, Azure, OVH Cloud)
* Infra / Network
* Equipment / End-user Devices
* Equipment / IoT
* Equipment / Industrial equipment
* Software / Development Tools
* Software / CI/CD
* Software / Backend
* Software / API
* Software / Mobile Apps (for example: Android App, iPhone App)
* Software / Web Apps (for example: React, Spring, Node.js, ROR, PHP apps)
* Software / Web Content (for example: WordPress, Drupal, Prestashop, Magento, etc.)
* TBQ: To be Qualified

## Assessed Functional Unit ([assessed_functional_unit])**✅**

Which granularity of a digital service or an information system can be assessed with the tool (it does not include the data used as entry point which are covered in the field [data_entry_point]):

* Process (System)
* Application
* Team
* Project
* User
* Request (http)
* Feature
* User Story
* Machine
* Room
* Website
* Network Traffic
* TBQ: To be Qualified

##  Data Entry point ([data_entry_point])**✅**

List all the data used to produce the environmental indicators.

* Server plan
* CPU based (RAPL)
* CPU, RAM, I/O (raw)
* Bandwidth
* DOM Size
* Request Number
* User Journey Modelisation
* User localization
* Datacenter Localization
* Connexion type
* PUE
* WUE
* Mutualization rate
* Devices Inventory (both internal and external users of an application)
* CPU capacity
* RAM capacity
* I/O Capacity
* Traffic/Usage
* Storage
* Undisclosed
* TBQ: To be Qualified

## Life Cycle Steps ([life_cycle_steps])**✅**

Qualify which steps of a Life Cycle Assessment are tracked. Minimum coverage is usually “usage” when only the energy consumed during the use phase is taken into consideration. This field enables also to qualify the scope(s) being covered for the GWP indicator (GHG emissions in CO2e). Usual steps of an [ISO 14040:2006 LCA](https://www.iso.org/standard/37456.html) are eligible:

* Extraction
* Manufacturing
* Transport
* Usage
* End of life
* Not Applicable
* Undisclosed
* TBQ: To be Qualified

## GHG scope covered ([ghg_scope])**✅**

This category makes it easy to link the product view (life cycle steps) with the Corporate Standard (company scopes), for educational purposes.

If GWP is checked in the environmental indicator field, this field indicates which scopes are covered (following [GHG protocol](https://ghgprotocol.org/) Corporate Standard):

* Scope 1 and 2 (market-based)
* Scope 1 and 2 (location-based)
* Scope 1, 2 (market-based) and 3
* Scope 1, 2 (location-based) and 3

Should be aligned with the Life Cycle Steps (no scope 3 can be indicated if Manufacturing is not included in the Life Cycle Steps).

![The relationship between the Corporate, Scope 3, and Product Standards for a companymanufacturing product A (Extracted from GHG Protocol Product Standard)](/api/attachments.redirect?id=8464dcbc-6acc-44e9-8a32-d40b0b0ef4a2 " =368x174")


## Focus ([focus])**✅**

The information can be provided by the organization itself or assessed by Boavizta team. This field describe the main goals of the tool, several values are allowed. This field is for classification purpose.

Goals can be:

* Reporting
* Calculation
* Awareness
* Eco-design
* Collection (of data)
* TBQ: To be Qualified

## Licence ([licence])**✅**

Describe the legal environment of the intellectual property of the tool:

* Open-Source under Apache 2.0 licence
* Open-Source under AGPLv3 licence
* Open-Source under GPLv2 licence
* Open-Source under GPLv3 licence
* Open-Source under BSD-3 licence
* Open-Source under MIT license
* Creative Commons (CC-BY-NC-ND)
* Creative Commons (CC-BY)
* Open-Source under an unkown licence
* Business Source - non permissive licence (the code is accessible but its licence restricts its permitted use such as no commercial use or internal use only if self-hosted; elasticsearch is an example)
* Closed Source / Commercial (the code isn’t shared)
* TBQ: To be Qualified

## Self-Hostable ([self_hostable])**✅**

Can the tool be self-hosted or is it only a SaaS solution?

* Yes
* No
* Not Applicable
* TBQ: To be Qualified

## Originating Country ([originating_country])**✅**

Where the legal entity owning the intellectual property of the tool is legally based. Value should be of [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) format. Several values are possible.

## Logo ([logo])**✅**

A URI pointing to an image file file. We recommand square image file with maximum size of 300x300px and maximum weight of 100Kb

## Inside Models ([inside_models])**✅**

Main models being used for the evaluation. This field requires “Assessment Type = Evaluation”. The possible values of this field are linked to the Models table listing existing models and their main academic references [NDR Once the repository will have been migrated from NocoDB to its final platform).

## Methodology transparency ([methodology_transparency])**🫂**

To which audience is disclosed the following information: inside model, main data sources and main scientific sources (single value):

* Undisclosed
* Disclosed only to internal stakeholders or clients
* Disclosed to a scientific panel who shared the results
* Disclosed to a scientific panel who did not share the results
* Fully Disclosed
* TBQ: To Be Qualified

## Transparency index ([transparency_index])**✅**

*[TBD in v2 A grade based on the completude of the fields of this repository]*

## Boavizta Processing Status ([status])**✅**

*[NDR To be updated once validation process will be finalized]*

Described where the recording stands in the listing process (single value):

* Submitted (ex-Sandbox): any record created by someone outside Boavizta or a Boavizta member willing to mention a tool to investigate
* Draft: all the required fields are complete and the other fields are filled in with the available information on the tool or the approriate flag (“Not Applicable”, “To Be Qualified”, etc.)
* Boavizta reviewed: a Boavizta member who is not the creator of the recording has reviewed and validated the recording. A boavizta member who is a stakeholder of an organization cannot reviewed any of its tool.
* Published: the recording is publicly exposed in the repository (database and API)
* Not to be listed: tool which don’t meet the criteria to be listed in the repository

## Reference Sources ([ref_sources]) **✅**

Must be URL with a path separated by comma. A list of the references supporting the claims about the tool made in this table (blog articles, scientific paper, white paper, presentation, webinar, etc.). The scientific paper linked to the model(s) used are optional because they are listed in the Model table.

# Models table [Models]

## Name of the Model ([model_name] [R]) **✅**

Examples of existing model: OneByte, Sustainable Webdesign, SimpleModel, GreenFrame, RAPL, CO2.js

## Model website or landing page ([model-site]) **🫂**

## Links to scientific papers ([scientific_papers] [R]) **✅**

Main research publication (peer reviewed only) describing the model and its upgrade.

## Main data sources ([main_data_source] [R])**✅**

Which data are used to build the model.

## Date of creation ([creation_date])**🫂**

## Organization ([model_organization] [R]) **🫂**

Which organization, research center or University promotes this model.

*NB Shall it be a multiple values field?* Shall it be connected to a link of academic papers?


