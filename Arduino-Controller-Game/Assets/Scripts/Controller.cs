using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controller : MonoBehaviour
{
    int xAxis = 1, yAxis = 1, buttonClick = 0;

     // Invoked when a line of data is received from the serial device.
    void OnMessageArrived(string msg)
    {
        Debug.Log("Message arrived: " + msg);

        var array = msg.Split(","[0]);
        xAxis = int.Parse(array[0]);
        yAxis = int.Parse(array[1]);
        buttonClick = int.Parse(array[2]);

        Debug.Log("x: " + xAxis + " y: " + yAxis);

        //center value 525|521|1

        if(xAxis < 1) transform.position += new Vector3(0.25f, 0f, 0);
        else if(xAxis > 1) transform.position -= new Vector3(0.25f, 0f, 0);

        if(yAxis < 1) transform.position -= new Vector3(0f, 0f, 0.25f);
        else if(yAxis > 1) transform.position += new Vector3(0f, 0f, 0.25f);

        if(buttonClick == 1) transform.position += new Vector3(0f, 1f, 0f);
    }

    // Invoked when a connect/disconnect event occurs. The parameter 'success'
    // will be 'true' upon connection, and 'false' upon disconnection or
    // failure to connect.
    void OnConnectionEvent(bool success)
    {
        if (success)
            Debug.Log("Connection established");
        else
            Debug.Log("Connection attempt failed or disconnection detected");
    }
}
