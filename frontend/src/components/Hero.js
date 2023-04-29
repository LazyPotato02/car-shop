import './Hero.css'

// import logoHero from './img/logo__hero.png'
import firstImage from './img/1.jpg'
import secondImage from './img/2.jpg'
import thirdImage from './img/3.jpg'
import fourthImage from './img/4.jpg'

function Hero() {
    return (

        <section className={'hero__section'}>
            <h1 className={'header__title'}>Car Store where you can rent or buy a car! </h1>



            <article className={'hero__first__about'} id={'hero'}>
                <img src={firstImage} alt=""/>
                <p>Looking to buy a new car? A car store might just be the place for you. Car stores are a one-stop-shop
                    for all your car buying needs. From brand new cars to used cars, from luxury vehicles to
                    budget-friendly options, car stores offer a wide variety of cars to choose from.</p>

            </article>
            <article className={'hero__second__about'}>
                <img src={secondImage} alt=""/>
                <p>At a car store, you'll have the opportunity to test drive cars and speak with knowledgeable
                    salespeople who can help you find the perfect vehicle for your needs and budget. Many car stores
                    also offer financing options, making it easier for you to afford the car of your dreams.</p>

            </article>
            <article className={'hero__third__about'}>
                <img src={thirdImage} alt=""/>
                <p>But car stores aren't just for buying cars. They also offer a range of services to help you maintain
                    your vehicle. From oil changes to tire rotations, car stores have experienced technicians who can
                    help keep your car running smoothly.</p>

            </article>
            <article className={'hero__fourth__about'}>
                <img src={fourthImage} alt=""/>
                <p>So whether you're in the market for a new car or just need some maintenance done on your current
                    vehicle, consider visiting a car store. With their wide selection of cars and knowledgeable staff,
                    you're sure to find exactly what you're looking for.</p>

            </article>
            <p id={'cars'} className={'header__second__title'}>Over 5000 cars available to purchase or rent!</p>

        </section>
    )
}

export default Hero