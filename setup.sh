export AUTH0_DOMAIN="fsnd-finalproject-burge.us.auth0.com"
export API_AUDIENCE="management"
export ALGORITHMS=["RS256"]
<<<<<<< HEAD
export CLIENT_SECRET="PnZGgR-m42u4e12Mpr81jgFc1J48O4mQBB6fNt6fQOZBu6hZ5bKdEQBMghcHLgHB"
export DATABASE_URL="postgres://localhost:5432/casting"
||||||| 157a1a4... ran pycodestyle on all files and moved sensitive data to setup.sh
export CLIENT_SECRET="PnZGgR-m42u4e12Mpr81jgFc1J48O4mQBB6fNt6fQOZBu6hZ5bKdEQBMghcHLgHB"
export DATABASE_URL="postgres://localhost:5432/casting"
export jwt_ep="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU3YjBkOGY3YmUyZjAwNmU3YTg2ZDAiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNjAwMjk2NDQ1LCJleHAiOjE2MDAzODI4NDUsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.MJc88QcQ0kP7xhyjJyuCVxHm08FpQSUlfKTDA9364zb9VD9NuGPCj3t_2LIN0ZM7t5M9hXg2f8KKqFetA3t6FMwJCa2jnZ5PVedVwD-ix9Zsgd5wrJYntsVwtM6QhRN8tvIvqrRCF0O5c4ugy2NAwz6Bd6BeZwMBr_L3aK8W0Ul5ucec6M6Ru_W32k5aoFDrjnlkCWJXgIy6JXnKGU5IF7vqoV1eJtKex6I_Mw8GPB5ega_Ggj_4bAtUNUOM7OewmxfymvGBRcwtIwqmBClddJyGRtdIYnhuPrYllZsOuhx3RSW9pOp9cUBA-LD3ZUsswTmeB2M-zvPeQ_64ejQFrA"
export jwt_cd="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU3YjBmNjA4MjRmOTAwNmVjOWQxZGMiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNjAwMjk2NDg3LCJleHAiOjE2MDAzODI4ODcsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.apULyCGVniCf58jQV0qb03oliKJzkGNt9-p-R1GD1S5qwX7G6gHagSEoKMKNNxvqqGD857edsFfbA8ziEaYCag3MLOB05oGComuZlT_Vv1UGuCoQce8iXkqz2-9AcwPjrlocGeOfKVAeL9ZZTu_bmIwBPfhDsbJRfc5WHX-kz8TXKynhKeNy572KZPHQpzKzfoYvkJo6_dtpBfYwBtGUTs1rwPuFiFpZnz26FfNfVBIQgz-zLfZY4ZhBdE3FugEasymNIgMRbdx2z10ufZk4ev6AODYwwFIFhKKUTrHOiW2bsEWP1H4MGsl5rKMW3wsstksOgRP2jLZIATt3wFDJKw"
export jwt_ca="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU3YjExNGRmZmYwNjAwNjgyZDEyMmMiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNjAwMjk2NTMwLCJleHAiOjE2MDAzODI5MzAsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.tycN1sIwUNP_b6lxA14Qf7JebJfF1WSmm-3qIGmpP6o-Axi3-OP5z9sMYUPzESoUdyUfkjrjijahSPB3yjGm6aN99JBCnCyLp98BlpS3OnkXngt100PKWo7da0FFme2Dw8OkIVDHCgpqP2mh9Al7Z54w1Bl91vyF18OYCms-MZ0duT32EavdnyI0-5pe7f_kgOhVSAH_Xi4qDCpeOTSzdByeg1lFWEAZgudh5Jxc9SkA85832YOPWTAluIKzUFJ4E-UukyU_zreTz7F8vPDV3xzfvmdbartR7Nqkre-sNW5ss5V15Ghf28-MUa6x7kHLgcwCWC_eS7jny0x8DdtKTw"
export jwt_no="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZIWG9XTGFJZk1od0tERjh2TEtTWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtZmluYWxwcm9qZWN0LWJ1cmdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjU5MmIyYWMwZTU5ZTAwNzZmMTJhNGIiLCJhdWQiOiJtYW5hZ2VtZW50IiwiaWF0IjoxNjAwMjk2NTc0LCJleHAiOjE2MDAzODI5NzQsImF6cCI6ImFDQTdFakF1VFcxaDhjWUJTOEJuUHo5bEtYdktxbGJNIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6W119.evHY3MgArQfLJWTRrutbCO19yh4dHv7lJKvyKxfsTc2fCPjk9yhuq79ZUr0BSfkhGns5UswoYLldSCcmamvV626gwbt3LvPBHJQUvt2mnXaYyzeKAg1vCKU7_ses2tAqs0bQSDIGwEnyUEJA8_fEWG1eno9Qy_kw0SVuINDkGClyPZ5FOUHx835JiOOzQLrHDiCb8LGY4hTcLxV3l-ufw9SnMisp8OhyemZfSeT0WsSsdVj1NIBpBOp_0CyDZ4FrIA2o9hsrAXnD2Cns-vmvZOCHKpBwvf9y6Qgfwa8NlysurgSeknME7s5S5MBEsHjiHywfBa--l9V79axW8wsRmQ"
=======
export DATABASE_URL="postgres://localhost:5432/casting"
>>>>>>> parent of 157a1a4... ran pycodestyle on all files and moved sensitive data to setup.sh
