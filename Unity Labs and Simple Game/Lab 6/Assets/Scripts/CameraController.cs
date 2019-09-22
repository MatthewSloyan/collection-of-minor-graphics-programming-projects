using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour {

	//allow unity to access the player object and set it.
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
		//allow the user to look around with the mouse in a realistic view
		yaw += speedH * Input.GetAxis ("Mouse X"); //get the input from the mouse and move accordingly
		pitch -= speedV * Input.GetAxis ("Mouse Y");

		transform.eulerAngles = new Vector3 (pitch, yaw, 0.0f);

		transform.position = player.transform.position + offset;
	}
}
