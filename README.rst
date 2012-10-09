Desk.com Advanced Template README
===============

All you need to know for working with custom Desk.com templates.

Help Center
-------------------

The Help Center uses a custom Desk.com web template named 'Gidsy support'.
* All the template files can be found in the Gidsy Git-repository at the location:
    gidsy/templates/desk/gidsy_template/

* When done editing, the code can be inserted in the Advanced Templates editor at:
    https://help.gidsy.com/admin/channels/support-center/web-templates

* The template uses an **external** CSS file, as well as an iconset. These are all hosted on S3 'gidsy-files'. See:
    gidsy/templates/desk/gidsy_template/desk.css
    gidsy/templates/desk/gidsy_template/images/


Email Templates
-------------------
All the email template files can be found in the git repo as well. See:
    gidsy/templates/desk/gidsy_template/gidsy_reply_template

* The template files use the 'simple' Gidsy email layout. Found in:
    gidsy/templates/emails/layout/simple.css

* This also means you have to add the simple.css into the Desk template files and run them through an inline-css tool. This is HTML commented in the Desk template files.