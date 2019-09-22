using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadScene2 : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {

		//when C is pressed load Demo Scene
		if (Input.GetKeyDown(KeyCode.C))
		{
			Debug.Log("C key was pressed.");
			SceneManager.LoadScene("Demo");
		}
	}
}
