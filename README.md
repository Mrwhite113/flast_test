How to run:
1. Cope remote repositorie to local: 
  
        git clone remote origin https://github.com/Mrwhite113/flast_test.git
 
2. Create virtual environment:

        python3 -m venv awesome_venv
 
3. Install python packegs:

        pip intsall -r requirements.txt
  
4. Import flask app variable:

        export FLASK_APP=main
   
   And start flask shell
        
        flask shell

5. Create db models in flask shell:

        from flast_test.apps.database.postgres.models import db
        db.create_all()
        
6. Run parcer of google sheet: 

        from flast_test.apps.crawler.parser import inset_data
        inset_data()

7. Run flask application

        flask run
