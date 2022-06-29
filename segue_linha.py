def control(left_sensor, right_sensor, speed):
    
    T = 10000 - 0.49 * speed * speed
    P = 0.3
    erro = right_sensor - left_sensor
    teta = P * erro
    if teta > 0.3:
        teta = 0.3     

    elif speed > 125:
        T = 500

    return {
        'engineTorque': T,
        'brakingTorque': 150,
        'steeringAngle': teta,
        'log': [
            { 'name': 'Speed', 'value': speed, 'min': 0, 'max': 100 },
            { 'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1 },
            { 'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1 }
        ]
    }
