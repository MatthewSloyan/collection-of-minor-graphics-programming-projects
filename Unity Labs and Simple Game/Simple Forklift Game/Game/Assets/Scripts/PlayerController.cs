using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {

	public GameObject player;
	private Vector3 offset;

	public float speedH = 2.0f;
	public float speedV = 2.0f;

	private float yaw = 0.0f;
	private float pitch = 0.0f;

	// Use this for initialization
	void Start () {
		//get the offset using the current player position
		offset = transform.position - player.transform.position;
	}
	
	// Update is called once per frame
	void Update () {
		yaw += speedH * Input.GetAxis ("Mouse X"); //get the input from the mouse and move accordingly
		pitch -= speedV * Input.GetAxis ("Mouse Y");

		transform.eulerAngles = new Vector3 (pitch, yaw, 0.0f);

		transform.position = player.transform.position + offset;
	}
}

//Documentation
//I created a basic forklift simulator. To do this I first downloaded a forklift asset and controlls from the store. I then downloaded an additional
//which contained the containers, boxes etc. I created a basic warehouse scene by adding in these assets to make the scene as realistic as possible and
//give the player an playground to drive around in/lift boxes etc. I also added in a first person camera to the forklift to increase realism.

//To play you can use WASD or the arrow keys to drive forward/back and turn. Then to lift the forklift you can use the PgUp and PgDn buttons.
