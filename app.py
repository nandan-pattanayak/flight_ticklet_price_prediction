from flask import Flask,request,url_for,render_template

import pickle
model = pickle.load(open('flight_price_regression.pkl', 'rb'))
app=Flask(__name__)
@app.route("/")
def hello():
	return render_template("index.html")
@app.route("/find",methods=['GET','POST'])
def find():
	if request.method=="POST":

		data1=request.form['Airline']
		airline_data=int(data1.split("(")[0])
		data2=request.form['Source']
		source_data=int(data2.split("(")[0])
		data3=request.form['Destination']
		destination_data=int(data3.split("(")[0])
		stops_data=int(request.form['stops'])
		date=int(request.form['date'])
		data4=request.form['month']
		month=int(data4.split("(")[0])
		final_data=[airline_data,source_data,destination_data,stops_data,date,month]
		final=[final_data]
		prediction=model.predict(final)
		output = round(prediction[0], 2)
		print(output)
	return render_template("result.html",prediction=output)

if __name__ == "__main__":
	app.run(debug=True)