import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component
{
  constructor(props)
  {
    super(props);
  }

  render()
  {
    return (
      <div>
        Welcome to Music Controller
      </div>
    );
  }
}

const appDiv = document.getElementById("app");

render(<App />, appDiv);