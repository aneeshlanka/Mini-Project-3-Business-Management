<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Aneesh Lanka (al762)</td></tr>
<tr><td> <em>Generated: </em> 4/11/2023 9:27:27 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/al762" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231027869-7f590013-93da-417e-bd4c-39e90ba17fab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of the index page with name and UCID changed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231031258-c1b2fa66-cdef-4991-9e30-3cc2aadd7b0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Companies tables not populated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231031357-ebd313b4-84c0-4662-8b52-da5b37bc1a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employees table not populated<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231031940-85163118-b950-492c-86b1-89e09b10a242.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message saying to upload only csv files<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231032094-8b8bf762-5f83-4951-ba5e-572c63b31cfa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message saying to upload some file to begin with<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231033157-8f1457de-9c37-44d6-990f-ac09cdd7059f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing the count of the data uploaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231032479-21cd3a5f-944b-4ef3-ac74-7cdb12384bbb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data uploaded into corresponding table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231033239-730ac618-d9c9-4dd0-8f57-c30d5f784cda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee data uploaded into corresponding table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asdf<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231033590-a0d51f47-f50a-44cd-b087-f30b47f641a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New employee data before submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231033747-209c1d73-69ac-4ca2-bd95-31aac6421fe0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New employee update confiemd<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231034022-89dad9da-1615-4312-9a3f-ba3fadf0b0fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name, last name &amp; mail error messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231034280-52dd4153-b195-4580-add0-7bf65f2f8213.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid employee added to the table - 1001 New Employee <a href="mailto:&#x6e;&#x65;&#119;&#x65;&#x6d;&#x70;&#x6c;&#111;&#x79;&#x65;&#x65;&#x40;&#103;&#x6d;&#x61;&#x69;&#108;&#46;&#99;&#x6f;&#x6d;">&#x6e;&#x65;&#119;&#x65;&#x6d;&#x70;&#x6c;&#111;&#x79;&#x65;&#x65;&#x40;&#103;&#x6d;&#x61;&#x69;&#108;&#46;&#99;&#x6f;&#x6d;</a><br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>adf<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ads<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231034787-15d94c18-54be-45b8-956d-888e971e0f82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with first name &#39;le&#39; as filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231034991-8951cdeb-16e9-48ce-97d0-3308b5b2a80d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with last name &#39;an&#39; as filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231035138-1841db78-c514-454a-9fb2-44c11c015ccb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with email as &#39;@hotmail.com&#39; as filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231035257-dba0447a-2f17-4041-b213-7e105c02b5cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with company as filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231035472-6a569eee-51c5-4524-92f0-200eb6d7ecc7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ascending email filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231035618-08e6ac0d-956c-491a-9408-d2451b2d49d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Descending email filter<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asdf<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asdf<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asdf<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231048484-500b3006-cd6a-43e0-abca-a86da53480b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Josephine Darakjy mail id will be changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231048770-e5cd7224-5c0b-4762-8671-e9d03741f836.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Josephine Darakjy mail id changed to <a href="mailto:&#74;&#68;&#64;&#x64;&#x61;&#114;&#97;&#x6b;&#106;&#121;&#x2e;&#x6f;&#114;&#x67;">&#74;&#68;&#64;&#x64;&#x61;&#114;&#97;&#x6b;&#106;&#121;&#x2e;&#x6f;&#114;&#x67;</a><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231049066-2a214837-d2fc-400d-a6d0-14254f9df97d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Josephine Darakjy mail id will be changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231049086-f3070404-ef4e-4c4c-9dc9-d8ea09d2aab7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Josephine Darakjy mail id changed to <a href="mailto:&#x4a;&#x44;&#x40;&#x64;&#97;&#114;&#x61;&#107;&#106;&#121;&#46;&#111;&#114;&#103;">&#x4a;&#x44;&#x40;&#x64;&#97;&#114;&#x61;&#107;&#106;&#121;&#46;&#111;&#114;&#103;</a><br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047055-9c58ec12-7e24-4427-9f6b-6300b112d8c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>retrievieng form data for name,adddress,state,city etc<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047049-5844445a-71c7-4bfd-9a7a-a20c5f5c1734.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash messages for name,address,city etc<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047045-28c43ed7-1762-4a8f-896e-12c5013b7654.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>insert statement, showing success flash message and exception statement<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047038-0ef27aed-2873-4bfe-a96d-15f445888a6b.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231047193-24e5a5c6-3bcb-4ed1-8638-c4f539df05e5.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231047590-7f3d7fe7-0491-47ad-9420-b346d477a5aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>submittted succesfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231047803-6b9c9220-9ad7-45c6-b906-c9436cec8c36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231048114-f6995769-1cbc-4c63-af5e-4ab454156d62.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047820-0c76d0e6-46b0-476e-89df-74cb0cd4560f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asdf<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047817-fbc9472e-239d-450a-ba0e-9763801f2ce2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asdf<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047816-c2df0272-fa18-4aaf-8307-2d58405df7ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asdf<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231047810-50df9800-8570-40cd-a872-ea27b6607a58.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231045748-96744c12-18ba-4cc7-a7c0-ddea00ee233b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>man as filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231046259-781deb9d-f696-405c-a266-e4b627639067.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>US as filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231046508-33463061-63db-41b5-88af-44f6c73df3b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>NY as filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231046656-9d0a51cc-27ae-41cc-8df8-b8c9e48beee6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ZIPCODE ascending<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231046716-e570fb2c-2714-45af-b859-97dbb6f1231d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ZIPCODE descending<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048063-241891df-c0aa-4b6e-83a6-a3050d5332bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request args for neme country etc<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048061-4701151a-d6da-40f5-b20b-30ac3dc70c24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048058-c067d98d-ace4-4478-bb0c-3d319a2ff20d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048056-a9258dc9-d6bd-41b4-a7c4-9142773e5d14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>select statement, flash message to show success, exception <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048053-311fee0c-25e5-414e-90c2-5f5d4cc41fba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>select query, exception statement and render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231044669-b0b27c4b-7137-40b6-8802-4c16b7a06ef6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Address of Chanay, Jeffrey A Esq is 4 B Blue Ridge Blvd<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231044976-cb2b8bfc-fd00-4d71-9295-de4e358e3153.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Address of Chanay, Jeffrey A Esq is changed to 4 B GREEN Ridge<br>Blvd<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231045448-497e3100-9ce4-4e10-8a4a-44f943b3e024.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Address of Chanay, Jeffrey A Esq is 4 B Blue Ridge Blvd<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231045478-5ea43d98-3ae7-4930-9723-32fc1ced3986.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Address of Chanay, Jeffrey A Esq is changed to 4 B GREEN Ridge<br>Blvd<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update statement, flash messages, exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048521-42969b36-124c-40e6-8f4b-08a8c5f2dc98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request args and redirect statement<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231037357-c2e800d8-5e04-40e4-844d-31f4f8c55570.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deletion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231037539-6a665908-2ee1-451b-ac99-4bd47ca7389d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deletion of <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048514-59a44bca-147f-4a9c-a4c7-8c10a0200103.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/63836995/231048521-42969b36-124c-40e6-8f4b-08a8c5f2dc98.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231037817-06e21344-d2fb-4e55-8d1c-7b0980ab3c6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deletion of Benton, John B Jr	6649 N Blue Gum St	New Orleans<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231038045-90e0ba90-e034-44e1-a7d7-1e0054de21ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deletion of Benton, John B Jr	6649 N Blue Gum St	New Orleans<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113073/231032946-9462715c-d36e-4bcc-8d53-79f470fd003e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases showing all as PASSED<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>During this assignment, I faced a few challenges that are common in web<br>development projects like debugging and troubleshooting errors in the code. It&#39;s easy to<br>make mistakes when working on a complex project like this, and identifying the<br>source of errors can be time-consuming. To help with this, I used logging<br>and debugging tools like the Python logging module and the Flask debugger to<br>track down errors and identify their causes.&nbsp;<div>I encountered some challenges when deploying the<br>application to Heroku. The deployment process involves many steps, including configuring environment variables<br>etc. I had to troubleshoot some issues with the deployment process, but ultimately<br>was able to successfully deploy the application.&nbsp;Overall, this project was a great learning<br>experience in web development, and taught me valuable lessons about security, debugging, documentation,<br>and deployment. These are all important skills that will serve me well in<br>future projects.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/al762" target="_blank">Grading</a></td></tr></table>
