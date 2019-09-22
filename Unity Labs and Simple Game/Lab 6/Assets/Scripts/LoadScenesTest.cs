using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadScenesTest : MonoBehaviour {

	// Use this for initialization
	void Start () {
	}
	
	// Update is called once per frame
	void Update () {
		//when C is pressed load SampleScene
		if (Input.GetKeyDown(KeyCode.C))
		{
			Debug.Log("C key was pressed.");
			SceneManager.LoadScene("SampleScene");
		}
	}
}