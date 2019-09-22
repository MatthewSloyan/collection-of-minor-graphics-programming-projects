using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeMovement : MonoBehaviour {

	public float speed;
	private Rigidbody rb;

	// Use this for initialization
	void Start () {
		rb = GetComponent<Rigidbody> ();
	}
	
	// Update is called once per frame
	void FixedUpdate () {

		//get user input, to apply force (doesn't work properly)
		//float moveHorizontal = Input.GetAxis ("Horizontal");
		//float moveVertical = Input.GetAxis ("Vertical");

		//Vector3 movement = new Vector3 (moveHorizontal, 0.0f, moveVertical);

		//add a force using speed and movement calculated
		//rb.AddForce (movement * speed);

		//log user inputs and translate accordlingly 
		if (Input.GetKeyDown(KeyCode.UpArrow))
		{
			Debug.Log("Up key was pressed.");
			transform.Translate(0, 0, 1);
		}

		if (Input.GetKeyDown(KeyCode.DownArrow))
		{
			Debug.Log("Down key was pressed.");

			transform.Translate(0, 0, -1);
		}

		if (Input.GetKeyUp(KeyCode.RightArrow))
		{
			Debug.Log("Right arrow key was released.");
			transform.Translate(1, 0, 0);
		}

		if (Input.GetKeyUp(KeyCode.LeftArrow))
		{
			Debug.Log("Left arrow key was released.");
			transform.Translate(-1, 0, 0);
		} 

		//if user enters space instaniate new cube
		if (Input.GetKeyUp(KeyCode.Space))
		{
			Debug.Log("Space key was released.");

			//create a new cube item in specific position
			GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
			cube.AddComponent<Rigidbody>();
			cube.transform.position = new Vector3(3, 3, -3);
		} 
	}
}
