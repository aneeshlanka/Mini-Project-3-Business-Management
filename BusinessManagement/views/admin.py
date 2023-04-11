import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
import csv
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        print(file.filename)
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        # DONE - TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        # UCID - al762 , date - 10-04-2023, checking whether file is .csv or else flash message
        if file.filename[-4:] != '.csv':
            flash('Only .csv files are accepted', "warning")
            return redirect(request.url)
        if file and secure_filename(file.filename):
            companies = []
            employees = []
            # DON'T EDIT
            company_query = """
            INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE 
                        address=values(address),
                        city=values(city),
                        country=values(country),
                        state=values(state),
                        zip=values(zip),
                        website=values(website)
            """
            # DON'T EDIT
            employee_query = """
             INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP3_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                        last_name = %(last_name)s, email = %(email)s, 
                        company_id = (SELECT id FROM IS601_MP3_Companies WHERE name=%(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            # UCID - al762, date - 10-04-2023
            reader = csv.DictReader(stream)
            
            company_required_fields = ['company_name', 'address', 'city', 'country', 'state', 'zip', 'web']
            employee_required_fields = ['first_name', 'last_name', 'email', 'company_name']

            for row in reader:
                # pass # todo remove
                print(row) #example
                # TODO importcsv-3 extract company data and append to company list 
                # as a dict only with company data if all is 
                # UCID - al762, date - 10-04-2023
                if all(field in row for field in company_required_fields):
                    company = {field.replace('company_name', 'name').replace('web','website'): row[field] for field in company_required_fields}
                    print("company: ", company)
                    companies.append(company)
                # TODO importcsv-4 extract employee data and append to employee list 
                # as a dict only with employee data if all is present
                # UCID - al762, date - 10-04-2023
                if all(field in row for field in employee_required_fields):
                    employee = {field: row[field] for field in employee_required_fields}
                    print("Employee: ", employee)
                    employees.append(employee)
               
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    # UCID - al762, date - 10-04-2023
                    flash(f"Inserted/Updated {len(companies)} companies", "message")
                    print(f"Inserted/Updated {len(companies)} companies", "message")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                # UCID - al762, date - 10-04-2023
                flash("No companies are Loaded", "info")
                # pass
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    # UCID - al762, date - 10-04-2023
                    flash(f"Inserted/Updated {len(employees)} Employees", "message")
                    print(f"Inserted/Updated {len(employees)} Employees", "message")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                 # TODO importcsv-8 display flash message (info) that no employees were loaded
                 # UCID - al762, date - 10-04-2023
                 flash("No Emplopyees are Loaded", "info")
                # pass
            try:
                result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                print(f"Result {result}")
            except Exception as e:
                    traceback.print_exc()
                    flash("There was an error counting session queries", "danger")
            print("returning the html page")
    return render_template("upload.html")
