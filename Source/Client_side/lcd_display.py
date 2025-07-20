import RPi.GPIO as GPIO
import time

LCD_CHR = True
LCD_CMD = False
     
LCD_LINE_1 = 0x80 
LCD_LINE_2 = 0xC0 
     
E_PULSE = 0.0005
E_DELAY = 0.0005
        
def variables(container):
    global LCD_RS 
    global LCD_E 
    global LCD_D4 
    global LCD_D5 
    global LCD_D6
    global LCD_D7
	
    global LCD_WIDTH
    
    LCD_RS = container[1]
    LCD_E  = container[2]
    LCD_D4 = container[3]
    LCD_D5 = container[4]
    LCD_D6 = container[5]
    LCD_D7 = container[6]
     
    LCD_WIDTH = container[0]    
    
    main()
 
def main():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)       
  GPIO.setup(LCD_E, GPIO.OUT)  
  GPIO.setup(LCD_RS, GPIO.OUT) 
  GPIO.setup(LCD_D4, GPIO.OUT) 
  GPIO.setup(LCD_D5, GPIO.OUT) 
  GPIO.setup(LCD_D6, GPIO.OUT) 
  GPIO.setup(LCD_D7, GPIO.OUT) 
 
  lcd_init()
 
def lcd_init():
  lcd_byte(0x33,LCD_CMD) 
  lcd_byte(0x32,LCD_CMD) 
  lcd_byte(0x06,LCD_CMD) 
  lcd_byte(0x0C,LCD_CMD) 
  lcd_byte(0x28,LCD_CMD) 
  lcd_byte(0x01,LCD_CMD) 
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
 
  GPIO.output(LCD_RS, mode)
 
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  lcd_toggle_enable()
 
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_show(message,line,delay):

   message = message.ljust(LCD_WIDTH," ")
    
   if line ==  1:
        lcd_byte(LCD_LINE_1, LCD_CMD)
   elif line == 2:
        lcd_byte(LCD_LINE_2, LCD_CMD)
 
   for i in range(LCD_WIDTH):
     lcd_byte(ord(message[i]),LCD_CHR)
  
   time.sleep(delay)

def lcd_clean(line):
    if line == 1:
        lcd_show("",1,0)
    elif line == 2:
        lcd_show("",2,0)
    elif line ==  3:
        lcd_show("",1,0)
        lcd_show("",2,0)

if __name__ == '__main__':
 
  try:
      con = [16,7,8,25,24,23,18]
      variables(con)
      lcd_show("Hello world!",1,2)
      lcd_clean(1)

  finally:      
    lcd_byte(0x01, LCD_CMD)
    lcd_show("Goodbye!",1,2)
    GPIO.cleanup()


