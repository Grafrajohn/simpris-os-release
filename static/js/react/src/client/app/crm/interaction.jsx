import React from 'react';
import {Table, Column, Cell} from 'fixed-data-table';
import {render} from 'react-dom';
import {InteractionTable} from './interactionTable.jsx';
//import {InteractionForm} from './interactionForm.jsx';

class Interaction extends React.Component {
  constructor(props) {
    super(props);
    this.tabwidth = window.innerHeight;
    this.calltype =
    this.state = {
      filteredDataList : []//,
      //sortBy: 'id',
      //sortDir: null
      //width: window.innerHeight
    };
  }

  render() {
    // var sortDirArrow = '';
    // if (this.state.sortDir !== null){
    //   sortDirArrow = this.state.sortDir === 'DESC' ? ' ↓' : ' ↑';
    // }
    return (
      <div className="col-xs-12">
        <div className="row">
          {this.state.showButton ? <button id="btnInteraction" onClick={ this.onButtonClick.bind(this) } className="btn btn-primary btn-sm">New Interaction</button> : null}
        </div>
        <br/>
          {this.state.showForm ? <InteractionForm /> : null}
        <InteractionTable src={this.props.tabwidth} />
      </div>
    );
  }
}

render(<Interaction/>, document.getElementById('interaction'));