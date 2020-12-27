import React from 'react'
import PropTypes from 'prop-types'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import parse from 'html-react-parser'

export default function Listing (props) {
    const {
        page
    } = props
    return (
        <div className="inner-container">
            <Row>
                <Col sm={6}>
                    <h1>{page.title}</h1>
                </Col>
            </Row>
            <Row>
                <Col sm={6}>
                    <Row>
                        {parse(page.description)}
                    </Row>
                    <Row>
                        <h3>Plan your trip to {page.title}</h3>
                        <p>Select a region using the map to your right or pick one from the drop down below.</p>
                        <br></br>
                    </Row>
                </Col>
                <Col sm={6}>
                    <img src={page.heroImage.jpeg800}/>
                </Col>
            </Row>
        </div>
    )
}

Listing.propTypes = {
    page: PropTypes.object.isRequired,
    handlePage: PropTypes.func
}
