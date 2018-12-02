
import math
import psycopg2
import secret

class Point:
    cordX = 0.0
    cordY = 0.0
    def _init__(self):
        self.cordX = 0.0
        self.cordY = 0.0
    def getX(self):
        return cordX
    def getY(self):
        return cordY
    def setX(self, newX):
        self.cordX = newX
    def setY(self, newY):
        self.cordY = newY
    def setPoint(self, newX, newY):
        self.cordX = newX
        self.cordY = newY
    def printPoint(self):
        print("X = " + str(self.cordX) + ", Y = " + str(self.cordY))
    def repositionX(self, offSet):
        self.cordX += float(offSet + 0.00)
    def repositionY(self, offSet):
        self.cordY += float(offSet + 0.00)
    def propShift(self, offsetX, offSetY, maxX, maxY):
        self.cordX += float(offSetX + 0.00)
        self.cordY += float(offSetY + 0.00)
        self.cordX /= math.sqrt(float(maxX^2 + maxY^2))
        self.cordY /= math.sqrt(float(maxX^2 + maxY^2))
    #Need to shift coordinates..
    def swiftyProtocol(self,minX,minY,maxX,maxY):
        self.cordX -= float(minX +0.00)
        self.cordY -= float(minY+0.00)
        distance = float(math.pow((maxX - minX),2) + math.pow((maxY-minY),2))
        self.cordX /= math.sqrt(distance)
        self.cordY /= math.sqrt(distance)
#To insert points into databse.
def dbPoints(imgName, points):
    connection = "host = 'localhost' dbname = 'learningflask' user='" + secret.theUser    + "' password='" +  secret.theSecret + "'"
    print("Connecting to database...")
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    query =""" Insert INTO picpoints (
    imgName,
    xCord01,
    yCord01,
    xCord02,
    yCord02,
    xCord03,
    yCord03,
    xCord04,
    yCord04,
    xCord05,
    yCord05,
    xCord06,
    yCord06,
    xCord07,
    yCord07,
    xCord08,
    yCord08,
    xCord09,
    yCord09,
    xCord10,
    yCord10,
    xCord11,
    yCord11,
    xCord12,
    yCord12,
    xCord13,
    yCord13,
    xCord14,
    yCord14,
    xCord15,
    yCord15,
    xCord16,
    yCord16,
    xCord17,
    yCord17,
    xCord18,
    yCord18,
    xCord19,
    yCord19,
    xCord20,
    yCord20,
    xCord21,
    yCord21,
    xCord22,
    yCord22,
    xCord23,
    yCord23,
    xCord24,
    yCord24,
    xCord25,
    yCord25,
    xCord26,
    yCord26,
    xCord27,
    yCord27,
    xCord28,
    yCord28,
    xCord29,
    yCord29,
    xCord30,
    yCord30,
    xCord31,
    yCord31,
    xCord32,
    yCord32,
    xCord33,
    yCord33,
    xCord34,
    yCord34,
    xCord35,
    yCord35,
    xCord36,
    yCord36,
    xCord37,
    yCord37,
    xCord38,
    yCord38,
    xCord39,
    yCord39,
    xCord40,
    yCord40,
    xCord41,
    yCord41,
    xCord42,
    yCord42,
    xCord43,
    yCord43,
    xCord44,
    yCord44,
    xCord45,
    yCord45,
    xCord46,
    yCord46,
    xCord47,
    yCord47,
    xCord48,
    yCord48,
    xCord49,
    yCord49,
    xCord50,
    yCord50,
    xCord51,
    yCord51,
    xCord52,
    yCord52,
    xCord53,
    yCord53,
    xCord54,
    yCord54,
    xCord55,
    yCord55,
    xCord56,
    yCord56,
    xCord57,
    yCord57,
    xCord58,
    yCord58,
    xCord59,
    yCord59,
    xCord60,
    yCord60,
    xCord61,
    yCord61,
    xCord62,
    yCord62,
    xCord63,
    yCord63,
    xCord64,
    yCord64,
    xCord65,
    yCord65,
    xCord66,
    yCord66,
    xCord67,
    yCord67,
    xCord68,
    yCord68
    ) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s ); """
    data = (
    imgName,
    points[0].cordX,
    points[0].cordY,
    points[1].cordX,
    points[1].cordY,
    points[2].cordX,
    points[2].cordY,
    points[3].cordX,
    points[3].cordY,
    points[4].cordX,
    points[4].cordY,
    points[5].cordX,
    points[5].cordY,
    points[6].cordX,
    points[6].cordY,
    points[7].cordX,
    points[7].cordY,
    points[8].cordX,
    points[8].cordY,
    points[9].cordX,
    points[9].cordY,
    points[10].cordX,
    points[10].cordY,
    points[11].cordX,
    points[11].cordY,
    points[12].cordX,
    points[12].cordY,
    points[13].cordX,
    points[13].cordY,
    points[14].cordX,
    points[14].cordY,
    points[15].cordX,
    points[15].cordY,
    points[16].cordX,
    points[16].cordY,
    points[17].cordX,
    points[17].cordY,
    points[18].cordX,
    points[18].cordY,
    points[19].cordX,
    points[19].cordY,
    points[20].cordX,
    points[20].cordY,
    points[21].cordX,
    points[21].cordY,
    points[22].cordX,
    points[22].cordY,
    points[23].cordX,
    points[23].cordY,
    points[24].cordX,
    points[24].cordY,
    points[25].cordX,
    points[25].cordY,
    points[26].cordX,
    points[26].cordY,
    points[27].cordX,
    points[27].cordY,
    points[28].cordX,
    points[28].cordY,
    points[29].cordX,
    points[29].cordY,
    points[30].cordX,
    points[30].cordY,
    points[31].cordX,
    points[31].cordY,
    points[32].cordX,
    points[32].cordY,
    points[33].cordX,
    points[33].cordY,
    points[34].cordX,
    points[34].cordY,
    points[35].cordX,
    points[35].cordY,
    points[36].cordX,
    points[36].cordY,
    points[37].cordX,
    points[37].cordY,
    points[38].cordX,
    points[38].cordY,
    points[39].cordX,
    points[39].cordY,
    points[40].cordX,
    points[40].cordY,
    points[41].cordX,
    points[41].cordY,
    points[42].cordX,
    points[42].cordY,
    points[43].cordX,
    points[43].cordY,
    points[44].cordX,
    points[44].cordY,
    points[45].cordX,
    points[45].cordY,
    points[46].cordX,
    points[46].cordY,
    points[47].cordX,
    points[47].cordY,
    points[48].cordX,
    points[48].cordY,
    points[49].cordX,
    points[49].cordY,
    points[50].cordX,
    points[50].cordY,
    points[51].cordX,
    points[51].cordY,
    points[52].cordX,
    points[52].cordY,
    points[53].cordX,
    points[53].cordY,
    points[54].cordX,
    points[54].cordY,
    points[55].cordX,
    points[55].cordY,
    points[56].cordX,
    points[56].cordY,
    points[57].cordX,
    points[57].cordY,
    points[58].cordX,
    points[58].cordY,
    points[59].cordX,
    points[59].cordY,
    points[60].cordX,
    points[60].cordY,
    points[61].cordX,
    points[61].cordY,
    points[62].cordX,
    points[62].cordY,
    points[63].cordX,
    points[63].cordY,
    points[64].cordX,
    points[64].cordY,
    points[65].cordX,
    points[65].cordY,
    points[66].cordX,
    points[66].cordY,
    points[67].cordX,
    points[67].cordY
    )

    cursor.execute(query,data)
    conn.commit()
    conn.close()