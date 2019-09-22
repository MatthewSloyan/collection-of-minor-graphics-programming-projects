using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shoot : MonoBehaviour {

	//initalize bullet prefab and spawn point
	public GameObject bulletPrefab;
	public Transform bulletSpawn;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyUp(KeyCode.R))
		{
			// Create the Bullet from the Bullet Prefab
			var bullet = (GameObject)Instantiate (
				bulletPrefab,
				bulletSpawn.position,
				bulletSpawn.rotation);

			// Add velocity to the bullet
			bullet.GetComponent<Rigidbody>().velocity = bullet.transform.forward * 7;

			// Destroy the bullet after 2 seconds
			Destroy(bullet, 2.0f);
		}
	}
}
