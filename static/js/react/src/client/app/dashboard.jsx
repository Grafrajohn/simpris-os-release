import React from 'react';
import {render} from 'react-dom';

class Dashboard extends React.Component {
  render () {
    return (
        <div className="col-xs-12">
            <div className="row">
                <div className="col-lg-12">

                    <div className="row">
                        <div className="col-lg-12">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Problems - (Morris Area charts v.02)</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div id="hero-area"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="row">
                        <div className="col-lg-12">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Morris Bar charts</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div id="graph-bar"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="row">
                        <div className="col-lg-6">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Different line charts</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div id="hero-graph"></div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-6">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Bar charts</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div id="hero-bar"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="row">
                        <div className="col-lg-6">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Area charts with multiple datasets</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div id="graph"></div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-6">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Donut flavours</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div id="hero-donut"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <h1>Knob charts</h1>
                    <div className="row">
                        <div className="col-lg-4">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Display previous value</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div className="center-block">
                                        <input className="knob" data-width="200" data-min="-100" data-fgColor="#03a9f4" data-displayPrevious="true" value="44"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-4">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>'cursor' mode</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div className="center-block">
                                        <input className="knob" data-width="200" data-cursor="true" data-fgColor="#90a4ae" data-thickness=".3" value="29"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-4">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Angle offset</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div className="center-block">
                                        <input className="knob" data-angleOffset="-125" data-angleArc="250" data-fgColor="#8bc34a" value="35"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="row">
                        <div className="col-lg-4">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Overloaded 'draw' method</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div className="center-block">
                                        <input className="knob" data-width="200" data-angleOffset="180" data-fgColor="#e84e40" data-skin="tron" data-thickness=".1" value="35"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-4">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Readonly</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div className="center-block">
                                        <input className="knob" data-fgColor="#ffc107" data-thickness=".4" data-readOnly="true" value="22"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-4">
                            <div className="main-box">
                                <header className="main-box-header clearfix">
                                    <h2>Infinite || iPod click wheel</h2>
                                </header>

                                <div className="main-box-body clearfix">
                                    <div className="center-block">
                                        <input className="infinite" data-width="200" data-thickness=".5" data-fgColor="#9c27b0" data-bgColor="#eeeeee" data-displayInput="false" data-cursor="true"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

		</div>
      )
  }
}

render(<Dashboard/>, document.getElementById('dashboard'));