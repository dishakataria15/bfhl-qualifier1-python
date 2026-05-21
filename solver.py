import requests

# Step 1: Generate webhook
gen_response = requests.post(
          "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
          json={"name": "Disha Kataria", "regNo": "1083", "email": "dishakataria231063@acropolis.in"}
)
data = gen_response.json()
webhook_url = data["webhook"]
access_token = data["accessToken"]

# Step 2: Submit SQL solution
final_query = """SELECT p.AMOUNT AS SALARY, CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME, TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE, d.DEPARTMENT_NAME FROM PAYMENTS p JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID WHERE DAY(p.PAYMENT_TIME) != 1 ORDER BY p.AMOUNT DESC LIMIT 1"""

response = requests.post(
          webhook_url,
          json={"finalQuery": final_query},
          headers={"Authorization": access_token, "Content-Type": "application/json"}
)

print(response.status_code, response.text)
