import React from 'react';
import {render} from 'react-dom';

class Lookup extends React.Component {
  render () {
    return (
        <div className="col-xs-12">
            <div className="row">
                <p>Some stuff here....</p>
            </div>
		</div>
      )
  }
}

render(<Lookup/>, document.getElementById('lookup'));