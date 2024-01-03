import React from 'react';
import {Table, Column, Cell} from 'fixed-data-table';
import {render} from 'react-dom';


export class InteractionForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        interactionTypes: [],
        interactions: []
    };
  }

  onButtonClick() {
      //alert('clicked!');
      //var _this = this;
      //this.setState({showForm: true, showButton: false});
      if ($("#txtDetail").val() === "") {
        $('#spnError').text("Please enter an interaction");
        return false;
      }

      var data = {
          details: $("#txtDetail").val(),
          type: $("#selInteractionType").find(":selected").val(),
          csrfmiddlewaretoken: simpris.csrf_token
      }

      $.ajax({
          url: '/api/interaction/insert/',
          method: 'POST',
          data: data,
          error: (function (err) {
              $('#spnError').text("There has been an error: " + err.statusText);
          }),
          success: (function (data) {
              //this.state.interaction = data;
              render();
              //
          })
      });
  }

  componentWillMount() {
        var _this = this;
      if (this.props.interactionid != undefined) {
          $.ajax({
              url: '/api/interaction/detail/' + this.props.interaction_id,
              type: 'GET',
              csrfmiddlewaretoken: '{{ csrf_token }}',
              error: (function (err) {
                  $('#spnError').text("There has been an error: " + err.statusText);
              }),
              success: (function (data) {
                  _this.setState({interaction: data});
              })
          });
      }

    $.ajax({
        url: '/api/lookup/lookups/22/',
        type: 'GET',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        error: (function (err) {
          $('#spnError').text("There has been an error: " + err.statusText);
        }),
        success: (function (data) {
          _this.setState({interactionTypes: data});
        })
    });
  }

  render() {
      var selectData = this.state.interactionTypes;
    return (
      <div className="col-xs-12">
        <form className="form">
            <div className="form-group">
                <select id="selInteractionType">
                    <option>Type of contact</option>
                    {
                        selectData.map((option) =>
                            <option value={option.lookupsubtypeid}>{option.lookupvaluechar}</option>
                        )
                    }
                </select>
            </div>
            <div className="form-group">
                <textarea id="txtDetail" className="form-control">
                </textarea>
            </div>
            <div className="form-group">
                <button id="btnAdd" className="btn btn-primary btn-small" onClick={ this.onButtonClick.bind(this) }>Add Interaction</button>
            </div>
        </form>
      </div>
    );
  }
}
