//http://allenfang.github.io/react-bootstrap-table/index.html
// with es6
import React from 'react'; // Import React
import { render } from 'react-dom'; // Import render method
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
var ReactBsTable = require("react-bootstrap-table");
import {InteractionForm} from './interactionForm.jsx';

export class InteractionTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            filteredDataList: [],
            showForm: false,
            showButton: true
        };
    }

    onButtonClick() {
      //alert('clicked!');
      //var _this = this;
      this.setState({showForm: true, showButton: false});
    }

    componentWillMount() {
      var _this = this;
      $.ajax({
          url: '/api/interaction/list/',
          type: 'GET',
          csrfmiddlewaretoken: simpris.csrf_token,
          error: (function (err) {
              $('#spnError').text("There has been an error: " + err.statusText);
          }),
          success: (function (data) {
              _this.setState({filteredDataList: data});
          })
      });
    }

    render() {
        return (
          <div className="col-xs-12">
            <div className="row">
              {this.state.showButton ? <button id="btnInteraction" onClick={ this.onButtonClick.bind(this) } className="btn btn-primary btn-sm">New Interaction</button> : null}
            </div>
            <br/>
              {this.state.showForm ? <InteractionForm /> : null}
            <div className="row">
                <BootstrapTable exportCSV data={this.state.filteredDataList} striped hover pagination>
                  <TableHeaderColumn isKey dataField='interactionid' dataSort={ true }>Interaction ID</TableHeaderColumn>
                  <TableHeaderColumn dataField='interactiontype' dataSort={ true }>Interaction Type</TableHeaderColumn>
                  <TableHeaderColumn dataField='details' filter={ { type: 'TextFilter', delay: 1000 } }>Details</TableHeaderColumn>
                  <TableHeaderColumn dataField='createddate' dataSort={ true }>Date</TableHeaderColumn>
                </BootstrapTable>
            </div>
          </div>
        );
    }
}