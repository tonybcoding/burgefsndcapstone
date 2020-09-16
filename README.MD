## Testing
***Local Unit Test***
The unit test provides thorough API endpoint testing covering all possible successes and entry errors. Also, since permissions are required, permissions of primary roles are tested. Thorough permission testing is available in the Remove test on heroku deployment below.

***Remote test on heroku deployment***
The remote test accessing the heroku deploymnet serves two purposes:
1. Prove effective deployment on heroku 
2. Attempt each endpoint action with each role provided success or failure based on permissions

### Local Unit Test
To run the local unit test, please following these steps:

1. Ensure casting database is in proper state by restoring the casting dabase to a local postgres instance. From the project root directory, run the following shell command:
    > psql -U postgres casting < casting.sql 
*(Note, you may change postgres in the shell command to a local user name)*

2. Set up environment. In project root, execute the following shell command
    > source ./env/Scripts/activate

3. Run local test script from root directory
    > python test_app_unit_local.py


### Remote test on heroku deployment
To run the remote test, please execute the following shell command in the project root directory:
> python test_app_hosted.py

The evaluator may query the contents of the remote database via the follow psql command:
> psql postgres://gjawgoezjiifnn:2a0a19c51a380c84e12c7baa64b51d7ecd46d7404cd96e6f87dd8b479842e4dc@ec2-3-215-207-12.compute-1.amazonaws.com:5432/d3emg2dn5g2cbp

