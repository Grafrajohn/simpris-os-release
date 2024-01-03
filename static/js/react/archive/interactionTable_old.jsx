import React from 'react';
import {Table, Column, Cell} from 'fixed-data-table';
import {render} from 'react-dom';
import {InteractionForm} from '../src/client/app/crm/interactionForm.jsx';

export class InteractionTable_old extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        filteredDataList : [],
        sortBy: 'interactionid',
        sortDir: null,
        width: window.innerHeight,
        rows: null,
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

  _renderHeader(label, cellDataKey) {
    return <div>
          <a onClick={this._sortRowsBy.bind(this, cellDataKey)}>{label}</a>
            <div>
              <br />
              <input style={{width:90+'%'}} onChange={this._onFilterChange.bind(this, cellDataKey)}/>
            </div>
        </div>;
  }

  _onFilterChange(cellDataKey, event) {
    if (!event.target.value) {
      this.setState({
        filteredDataList: this.rows,
      });
    }
    var filterBy = event.target.value.toString().toLowerCase();
    var size = this.rows.length;
    var filteredList = [];
    for (var index = 0; index < size; index++) {
      var v = this.rows[index][cellDataKey];
      if (v.toString().toLowerCase().indexOf(filterBy) !== -1) {
        filteredList.push(this.rows[index]);
      }
    }
    this.setState({
      filteredDataList: filteredList,
    });
  }

  _sortRowsBy(cellDataKey) {
    var sortDir = this.state.sortDir;
    var sortBy = cellDataKey;
    if (sortBy === this.state.sortBy) {
      sortDir = this.state.sortDir === 'ASC' ? 'DESC' : 'ASC';
    } else {
      sortDir = 'DESC';
    }
    var rows = this.state.filteredDataList.slice();
    rows.sort((a, b) => {
      var sortVal = 0;
      if (a[sortBy] > b[sortBy]) {
        sortVal = 1;
      }
      if (a[sortBy] < b[sortBy]) {
        sortVal = -1;
      }

      if (sortDir === 'DESC') {
        sortVal = sortVal * -1;
      }
      return sortVal;
    });

    this.setState({sortBy, sortDir, filteredDataList : rows});
  }

  render() {

    var parentWidth = $("#interaction").width();
    var workingWidth = parentWidth - (parentWidth * .05)
    var sortDirArrow = '';
    if (this.state.sortDir !== null){
      sortDirArrow = this.state.sortDir === 'DESC' ? ' ↓' : ' ↑';
    }
    return (
      <div className="col-xs-12">
        <div className="row">
          {this.state.showButton ? <button id="btnInteraction" onClick={ this.onButtonClick.bind(this) } className="btn btn-primary btn-sm">New Interaction</button> : null}
        </div>
        <br/>
          {this.state.showForm ? <InteractionForm /> : null}
        <div className="row">
          <Table className="table-responsive"
            height={35+((this.state.filteredDataList.length) * 90)}
            width={workingWidth}
            rowsCount={this.state.filteredDataList.length}
            rowHeight={90}
            headerHeight={30}
            rowGetter={function(rowIndex) {return this.state.filteredDataList[rowIndex]; }.bind(this)}>
            <Column dataKey="interactionid" width={workingWidth * 0.1}
              label={'Interaction ID' + (this.state.sortBy === 'interactionid' ? sortDirArrow : '')}
              headerRenderer={this._renderHeader.bind(this)}/>
            <Column dataKey="createddate" width={workingWidth * 0.3} label={'Date' + (this.state.sortBy === 'createddate' ? sortDirArrow : '')}
              headerRenderer={this._renderHeader.bind(this)}/>
            <Column  dataKey="details" width={workingWidth * 0.599} label={'Details' + (this.state.sortBy === 'details' ? sortDirArrow : '')}
              headerRenderer={this._renderHeader.bind(this)}/>
          </Table>
        </div>
      </div>
    );
  }
}
