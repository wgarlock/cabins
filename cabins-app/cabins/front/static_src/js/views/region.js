/* globals context */
import React from 'react'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default function Region () {
    return (
        <>
            <Row>
                <Col sm={6}>
                    <h1 className="page-title">{context.page.title}</h1>
                </Col>
            </Row>
            <Row>
                <Col sm={4}>
                    <Card >
                        <Card.Body>
                            <Card.Title>Filter by:</Card.Title>
                            <Card.Text>
                                <Form>
                                    <div key={'default-checkbox'} className="mb-3 filters-form">
                                        <h6>Suitability</h6>
                                        <Form.Check
                                            type="checkbox"
                                            id={'default-checkbox'}
                                            label={'default checkbox'}
                                        />
                                    </div>
                                    <div key={'default-checkbox'} className="mb-3 filters-form">
                                        <h6>Room</h6>
                                        <Form.Check
                                            type="checkbox"
                                            id={'default-checkbox'}
                                            label={'default checkbox'}
                                        />
                                    </div>
                                    <div key={'default-checkbox'} className="mb-3 filters-form">
                                        <h6>General</h6>
                                        <Form.Check
                                            type="checkbox"
                                            id={'default-checkbox'}
                                            label={'default checkbox'}
                                        />
                                    </div>
                                </Form>
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </Col>
                <Col sm={8}>
                    <Card>
                        <Row>
                            <Col sm={3}>
                                <Card.Img variant="top" src="holder.js/100px180" />
                            </Col>
                            <Col sm={9}>
                                <Card.Body>
                                    <div className="listingCard">
                                        <Card.Title>Card Title</Card.Title>
                                        <Card.Text>
                                            Some quick example text to build on the card title and make up the bulk of
                                            the cards content.
                                        </Card.Text>
                                    </div>
                                    <Button variant="secondary" className="mx-3">View</Button>
                                    <Button variant="primary" className="mx-3">Website</Button>
                                </Card.Body>
                            </Col>
                        </Row>
                    </Card>
                </Col>
            </Row>
        </>
    )
}
