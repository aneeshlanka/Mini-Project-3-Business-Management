from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import re
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    # UCID al762, Date - 10-04-2023
    query = """SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, IF(name is not null, name, 'N/A') as company_name
     FROM IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = [("id","Id"),("first_name", "First Name"), ("last_name", "Last Name"), ("email", "Email"), ("company_id", "Company Id"), ("company_name", "Company Name")]

    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fname = request.args.get('fn')
    lname = request.args.get('ln')
    email_address = request.args.get('email')
    company = request.args.get('company')
    col = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')

    # TODO search-3 append like filter for first_name if provided
    if fname:
        query += " AND e.first_name LIKE %(fname)s"
        args["fname"] = f"%{fname}%"

    # TODO search-4 append like filter for last_name if provided
    if lname:
        query += " AND e.last_name LIKE %(lname)s"
        args["lname"] = f"%{lname}%"

    # TODO search-5 append like filter for email if provided
    # UCID al762, Date - 10-04-2023
    if  email_address:
        query += " AND e.email LIKE %(email_address)s"
        args["email_address"] = f"%{email_address}%"

    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND e.company_id = %(company)s"
        args["company"] = company

    print(col, order)
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if col and order and col in ['first_name', 'last_name', 'email', 'company_name'] and order in ["asc", "desc"]:
        query += f" ORDER BY {col} {order.upper()}"

    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit:
        try:
            
            if int(limit) >100 or int(limit) <1:
                raise ValueError
        except ValueError:
            # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
            flash("ERROR. Limit is not in between 1 and 100")
            limit = 10
    else:
        limit = 10

    query += " LIMIT %(limit)s"
    args["limit"] = int(limit)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        print(e)
        flash("attention!! There was an issue while searching for employees.")   
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # TODO add-5a verify email is in the correct format
        # UCID al762, Date - 10-04-2023
        has_error = False # use this to control whether or not an insert occurs
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        company = request.form.get('company')
        email = request.form.get('email')

        # Validate required fields
        if not first_name:
            flash('pleast enter the first name')
            has_error = True
        if not last_name:
            flash('please enter the last name')
            has_error = True
        if not email:
            flash('please enter the email')
            has_error = True
        elif not re.match(email_pattern, email):
            flash('please enter the email in correct format')
            has_error = True
        
        args = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'company_name': company
        }

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP3_Companies WHERE name = %(company_name)s LIMIT 1))
                    ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                    last_name = %(last_name)s, email = %(email)s, 
                    company_id = (SELECT id FROM IS601_MP3_Companies WHERE name=%(company_name)s LIMIT 1)
                """, args
                ) # <-- TODO add-6 add query and add arguments
                # UCID al762, Date - 10-04-2023
                if result.status:
                    flash("Employee Record has been created successfully")
            except Exception as e:
                # TODO add-7 make message user friendly
                print(str(e))
                flash("Exception arised whin adding the Employee details!!")
    return render_template("add_employee.html")


@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # UCID al762, Date - 10-04-2023
    id = request.args.get("id")
    if not id:
        flash("Please enter the Employee ID")
        return redirect(url_for("employee.search"))
    else:
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            company_id = request.form.get("company")
            email = request.form.get("email")

            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            has_error = False
            # TODO edit-2 first_name is required (flash proper error message)
            # UCID al762, Date - 10-04-2023
            if not first_name:
                flash("Please enter the First name")
                has_error = True
            # TODO edit-3 last_name is required (flash proper error message)
            if not last_name:
                flash("Please enter the Last name")
                has_error = True
            # TODO edit-4 company (may be None)
            # company_id will be None if no value was selected in the form
            # we don't need to do any validation for this field
            # TODO edit-5 email is required (flash proper error message)
            if not email:
                flash("please enter the Email")
                has_error = True
            else:
                # TODO edit-5a verify email is in the correct format
                if not re.match(email_pattern, email):
                    flash("please re-enter the email in valid format")
                    has_error = True

            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    # UCID al762, Date - 10-04-2023
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees SET
                    first_name=%(first_name)s,
                    last_name=%(last_name)s,
                    company_id=%(company_id)s,
                    email=%(email)s
                    WHERE id=%(id)s;
                    """, {"first_name": first_name, "last_name": last_name, "company_id": company_id, "email": email, "id": id})
                    if result.status:
                        flash("record is updated succesfully")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash("Error has been detected while updating employee record.")
                    print(e)

        row = {}
        try:
            # TODO edit-8 fetch the updated data
            # UCID al762, Date - 10-04-2023
            result = DB.selectOne("""SELECT
            IS601_MP3_Employees.id AS id,
            IS601_MP3_Employees.first_name AS first_name,
            IS601_MP3_Employees.last_name AS last_name,
            IS601_MP3_Employees.email AS email,
            IS601_MP3_Employees.company_id AS company_id
            FROM IS601_MP3_Employees LEFT JOIN IS601_MP3_Companies
            ON IS601_MP3_Employees.company_id = IS601_MP3_Companies.id
            WHERE IS601_MP3_Employees.id =  %(id)s;""", {"id": id})
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("Employee record cannot be retrieved due to an upexcected error.")
            print(e)

    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", row=row)#, company_dropdown=company_dropdown)


@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # UCID al762, Date - 10-04-2023
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %(id)s;", {"id": id})
            if result.status:
                flash("Employee has been successfully deleted")
        except Exception as e:
            flash("Error!! Employee record cannot be deleted")
            print(e)

        # TODO delete-3 pass all arguments except id to this route
        args = {k: v for k, v in request.args.items() if k != "id"}
        # TODO delete-2 redirect to employee search
        return redirect(url_for("employee.search", **args))
    else:
        # TODO delete-5 if id is missing, flash necessary message and redirect to search
        flash("Please enter the Employee ID ")
        return redirect(url_for("employee.search"))
