# USB-RTC

<img src ="https://cdn.shopify.com/s/files/1/1217/2104/files/USB_RTC_8549f019-f1f0-415a-afa3-d2273adb42be.png?v=1669091063" />

USB RTC is an open source real time clock device that comprises MCP2221, a USB-to-UART/I2C serial converter, which enables USB connectivity, in the processes that include a USB, UART(Serial), GPIO, and I2C interfaces. 

## Installation on Raspberry Pi

* Install MCP2221 Library by running below command on terminal:

``` sudo pip3 install PyMCP2221A ```
              
* Connect USB-RTC on USB Port of Raspberry Pi.
* Now clone/download USB-RTC Github Repository by running below command:

```git clone https://github.com/sbcshop/USB-RTC-Software.git ```

* Now, open downloaded folder from home/pi or by running below command:

``` cd USB-RTC-Software/Examples ```

* Now run test.py file by running below command(Note : sudo should be added before running the file):

**```sudo python3 test.py ```**

## Installation on Windows

* Install MCP2221 Library by running below command on terminal:

``` pip install PyMCP2221A ```
              
* Connect USB-RTC on USB Port of Windows USB Port.

* Now clone/download USB-RTC-Software Github Repository by running below command:

```git clone https://github.com/sbcshop/USB-RTC-Software.git ```

* By running above command a folder (USB-RTC-Software) of this repository will be downloaded in your System.

* Now open the downloaded folder and run test.py file by running below command:

```python3 test.py ``` or directly run test.py in any python supported IDE (like Thonny).

## Functions

* To modify Date & Time, you have to change the last value of each line in hexadecimal form inside ```def SetTime(address):```

For Example : ``` bus.write_byte_data(0x68, 0x00, 0x02) # set seconds and start clock ``` , it will set second value as 02 second after executing  ```SetTime(address) ``` function.

* To read time , you can call ```ReadTime(address)``` Function
* To read internal temperature of USB-RTC, uncomment below line by removing ''' from start and end of the line :

    ```python Celsius = getTemp(address)
       Fahrenheit = 9.0/5.0 * Celsius + 32
       print (Fahrenheit, "*F /", Celsius, "*C") 
       
## Related Products

* [SquaryPi](https://shop.sb-components.co.uk/products/squary?variant=40443840921683)

 ![SquaryPi](https://cdn.shopify.com/s/files/1/1217/2104/products/1_5874b3b5-2a2f-453e-bf54-abbf2a26acb9.png?v=1670307456&width=400)

* [EncroPi](https://shop.sb-components.co.uk/products/encropi?_pos=1&_sid=95f822d26&_ss=r)

 ![EncroPi](https://cdn.shopify.com/s/files/1/1217/2104/products/03_a6b155c1-da03-427d-ba6a-44730c56d73f.png?v=1668595812&width=400)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>

