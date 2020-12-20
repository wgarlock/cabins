/* globals context */
import React from 'react'
import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'
import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'
import DatePicker from 'react-datepicker'

export default function Home () {
    let backgroundImage = null
    if (context.page.hero_image.jpeg_1960_url) {
        backgroundImage = context.page.hero_image.jpeg_1960_url
    }

    const jumboStyle = {
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        height: '400px'
    }

    return (
        <Jumbotron style={jumboStyle} fluid className="cabins-home-jumbo">
            <Container >
                <h1> Resorts &amp; Lodges </h1>
                <Form>
                    <Form.Row>
                        <Col xs={7}>
                            <Form.Control placeholder="Where?" />
                        </Col>
                        <Col>
                            <DatePicker style={{ color: '#000' }}/>
                        </Col>
                        <Col>
                            <Button variant="primary">Submit</Button>
                        </Col>
                    </Form.Row>
                </Form>
            </Container>
        </Jumbotron>
    )
}
