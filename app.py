from flask import Flask,request,jsonify
import math
app = Flask(__name__)
@app.route('/hello/<var>', methods = ['GET'] )
def hello(var):
  return f"Hi,{var}"
@app.route('/square/<int:number>')
def square_number(number):
    return jsonify({
        "number": number,
        "square": number ** 2
    }) 
@app.route('/quadratic/<float:a>/<float:b>/<float:c>', methods = ['GET'])
def quadratic(a,b,c):
   discriminant = b**2 - 4*a*c
   if discriminant < 0:
      return jsonify({"error": "No real roots exist as the discriminant is negative."}), 400
   root_1 = (-b + math.sqrt(discriminant))/(2*a)
   print('first root',root_1)
   root_2 = (-b - math.sqrt(discriminant))/(2*a)
   print('second root',root_2)
   return jsonify({
    "first root": root_1,
    "second root": root_2
  })
@app.route('/pressure/<float:area>/<float:force>', methods = ['GET'])
def pressure(area, force):
  pressure_value = force / area
  if pressure_value < 0:
    return jsonify({"error":"pressure is less than zero"}), 400
  else:
    return jsonify({
      "pressure": pressure_value
    })
@app.route('/orbital-speed/<int:radius>/<int:time>')
def orbital(radius,time):
   orbital_speed = (radius * 2 * math.pi) / time
   return jsonify({
      "orbital-speed": orbital_speed
   }) 
@app.route('/pythagoras/<int:base>/<int:height>')
def pythagoras(base,height):
   hyp = math.sqrt((base ** 2) + (height ** 2))
   return jsonify({
      "hypotenuse": hyp
   })
@app.route('/cube/<int:number>')
def cube(number):
   cube_value = number ** 3
   return jsonify({
      "cube": cube_value
   })
@app.route('/square-root/<int:number>')
def sqrt(number):
   square_root = math.sqrt(number)
   return jsonify({
      "square root": square_root
   })
@app.route('/cube-root/<int:number>')
def cube_rt(number):
   crt = math.cbrt(number)
   return jsonify({
      "cube root": crt
   })
@app.route('/power-x/<int:number>/<int:x>')
def power(number,x):
   pwer = number ** x
   return jsonify({
      "answer": pwer
   })
@app.route('/divide/<int:x>/<int:y>')
def divide(x,y):
   div = x / y
   return jsonify({
      "answer": div
   })
@app.route('/multiply/<int:x>/<int:y>')
def multiply(x,y):
   multiple = x * y
   return jsonify({
      "answer": multiple
   })
@app.route('/kinetic-energy/<int:mass>/<int:velocity>')
def E_K(mass,velocity):
   energy = ((velocity ** 2) * mass) / 2
   return jsonify({
     "Kinetic Energy":energy
   })
@app.route('/gravitiational-potential-energy/<int:mass>/<int:height>')
def G_P_E(mass,height):
   gpe = mass * height * 9.81
   return jsonify({
      "Gravitational Potential Energy": gpe
   })
@app.route('/acceleration/<int:velocity>/<int:time>')
def accelaration(velocity,time):
   acc = velocity / time
   return jsonify({
      "acceleration":acc
   })
@app.route('/area-trapezium/<int:a>/<int:b>/<int:h>')
def trapezium(a,b,h):
   trap = ((a + b) * h)
   return jsonify({
      "area": trap
   })
@app.route('/volume-cone/<int:radius>/<int:height>')
def cone(radius,height):
   volume = (((radius ** 2) * height) * math.pi) / 3
   return jsonify({
      "volume": volume
   })
@app.route('/volume-sphere/<int:radius>')
def sphere(radius):
   volume = (4 * math.pi * (radius ** 3)) / 3
   return jsonify({
      "volume": volume
   })
# @app.route('/')
if __name__ == '__main__':
  app.run(debug = True)