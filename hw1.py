from PIL import Image

im = Image.open("Penguins.jpg")
pixel = im.load()
width, height = im.size


# Q1. RGB three layer penguins
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        if (0 <= x and x < width / 3):
            pixel[x,y] = (R*3, G, B)
        elif (width / 3 <= x and x < width * 2 / 3):
            pixel[x,y] = (R, G*3, B)
        else:
            pixel[x,y] = (R, G, B*3)
im.save("Q1.jpg")



# Q2. CMYK four layer penguins
im = Image.open("Penguins.jpg")
out = im.convert("CMYK")
pixel = out.load()
for x in range(width):
    for y in range(height):
        C, M, Y, K = pixel[x,y]
        if ( (0 <= x) and (x < (width/4) ) ):
            pixel[x,y] = (C*3, M, Y, K)
        elif ( ((width/4) <= x) and (x < (width/2)) ):
            pixel[x,y] = (C, M*3, Y, K)
        elif ( ((width/2) <= x) and (x < (width*3/4)) ):
            pixel[x,y] = (C, M, Y*3, K)
        else:
            pixel[x,y] = (C, M, Y, K*3)
out.save("Q2.jpg")



# Q3. complementary colours penguins
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = (abs(R-255), abs(G-255), abs(B-255))
im.save("Q3.jpg")



# Q4. piexlated (mosaic) penguin
im = Image.open("Penguins.jpg")
pixel = im.load()
paradigm = []
for x in range(width):
    for y in range(height):
        if (x % 8 == 0 and y % 8 == 0):
            if ( (x/8) > 0 and y == 0):
                del paradigm[:]
            R, G, B = pixel[x,y]
            paradigm.append((R,G,B))
        elif (x % 8 != 0 or y % 8 != 0):
            pixel[x,y] = paradigm[int(y/8)]
im.save("Q4.jpg")



# Q5. gray-level penguin

##### (R+G+B)/3 #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = ((R+B+G)/3, (R+B+G)/3, (R+B+G)/3)
im.save("Q5-1.jpg")

##### 0.299*R + 0.587*G + 0.114*B #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = (int( 0.299*R + 0.587*G + 0.114*B ), int( 0.299*R + 0.587*G + 0.114*B ), int(0.299*R + 0.587*G + 0.114*B))
im.save("Q5-2.jpg")



# Q6. black-and-white penguin

##### Threshold = 20 #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        if((R+B+G)/3 < 20):
            pixel[x,y] = (0, 0, 0)  # black
        else:
            pixel[x,y] = (255, 255, 255)    # white
im.save("Q6-20.jpg")

##### Threshold = 64 #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        if((R+B+G)/3 < 64):
            pixel[x,y] = (0, 0, 0)  # black
        else:
            pixel[x,y] = (255, 255, 255)    # white
im.save("Q6-64.jpg")

##### Threshold = 180 #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        if((R+B+G)/3 < 180):
            pixel[x,y] = (0, 0, 0)  # black
        else:
            pixel[x,y] = (255, 255, 255)    # white
im.save("Q6-180.jpg")



# Q7. RGB -> RBG/ GRB/ GBR/ BRG/ BGR penguin

##### RGB -> RBG #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = (R, B, G)
im.save("Q7-RBG.jpg")

##### RGB -> GRB #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = (G, R, B)
im.save("Q7-GRB.jpg")

##### RGB -> GBR #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = (G, B, R)
im.save("Q7-GBR.jpg")

##### RGB -> BRG #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = (B, R, G)
im.save("Q7-BRG.jpg")

##### RGB -> BGR #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        pixel[x,y] = (B, G, R)
im.save("Q7-BGR.jpg")



# Q8. color-replaced penguin
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        if ( ( ((255-R)**2 + (190-G)**2 + (25-B)**2)**0.5 ) < 100.0 ):
            pixel[x,y] = (R, int(G*0.6), B)
im.save("Q8.jpg")



# Q9. line-drawing penguin
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        if (x < width-1 and y < height-1):
            R, G, B = pixel[x,y]
            R_down, G_down, B_down = pixel[x,y+1]
            R_right, G_right, B_right = pixel[x+1,y]
            if( abs( (R+B+G)/3 - (R_down+B_down+G_down)/3 ) > 10.0 and 
                abs( (R+B+G)/3 - (R_right+B_right+G_right)/3 ) > 10.0 ):
                pixel[x,y] = (0, 0, 0)  # black
            else:
                pixel[x,y] = (255, 255, 255)    # white
        else:
            pixel[x,y] = (0, 0, 0)  # black
im.save("Q9.jpg")



# Q10. remove noice penguin
im = Image.open("Penguins_noise.jpg")
pixel = im.load()
for x in range(1,width-1):
    for y in range(1,height-1):
        neighbor = [pixel[x-1,y-1], pixel[x,y-1], pixel[x+1,y-1],
                    pixel[x-1,y], pixel[x,y], pixel[x+1,y],
                    pixel[x-1,y+1], pixel[x,y+1], pixel[x+1,y+1]]
        neighbor.sort();
        pixel[x,y] = neighbor[4]
im.save("Q10.jpg")



# Q11. mirror image penguin

##### right to left #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        if ( x >= (width/2)):
            R, G, B = pixel[(width-x-1),y]
            pixel[x,y] = (R, G, B)
im.save("Q11-right_to_left.jpg")

##### left to right #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        if ( x < (width/2)):
            R, G, B = pixel[(width-x-1),y]
            pixel[x,y] = (R, G, B)
im.save("Q11-left_to_right.jpg")

##### top to bottom #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        if ( y >= (height/2)):
            R, G, B = pixel[x,(height-y-1)]
            pixel[x,y] = (R, G, B)
im.save("Q11-top_to_bottom.jpg")

##### bottom to top #####
im = Image.open("Penguins.jpg")
pixel = im.load()
for x in range(width):
    for y in range(height):
        if ( y < (height/2)):
            R, G, B = pixel[x,(height-y-1)]
            pixel[x,y] = (R, G, B)
im.save("Q11-bottom_to_top.jpg")



# Q12. Elsa + background
im = Image.open("Elsa.jpg")
bg = Image.open("Chrysanthemum.jpg")
pixel = im.load()
pixel_bg = bg.load()
for x in range(width):
    for y in range(height):
        R, G, B = pixel[x,y]
        R_bg, G_bg, B_bg = pixel_bg[x,y]
        if ( ( ((30-R)**2 + (27-G)**2 + (84-B)**2)**0.5 ) < 23.0 ):
            pixel[x,y] = (R_bg, G_bg, B_bg)
im.save("Q12.jpg")
