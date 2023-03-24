import './Hero.css'
import logoHero from './img/logo__hero.png'

function Hero() {
    return (
        <section>
            <div className={'hero__wrapper'}>

                <article className={'short__about'}>
                    <h1 className={'hero__title'}>Wellcome to Car Shop Store</h1>
                    Find your dream car at our web store! We offer a wide selection of
                    new
                    and used vehicles from top brands, hassle-free financing options, and thorough inspections for your
                    peace of mind. Start browsing today and drive off in the car you've always wanted!
                </article>
                <img className={'logo__hero'} src={logoHero} alt="logo_hero"/>
            </div>
            <article className={'about'}>
                <h2>About</h2>
                <ul>
                    <li>Welcome to our online car web store, where you can find the perfect vehicle to fit your
                        lifestyle and budget. We offer a wide selection of new and used cars from some of the most
                        popular brands in the industry, including Honda, Toyota, Ford, and etc..
                    </li>
                    <li>Our knowledgeable and friendly staff is dedicated to providing you with a hassle-free car buying
                        experience. Whether you're looking for a family sedan, a rugged SUV, or a sleek sports car,
                        we've got you covered. We offer a variety of financing options to help you get behind the wheel
                        of your dream car, including lease and loan options.
                    </li>
                    <li>At our car web store, we believe in transparency and honesty in all our dealings with our
                        customers. That's why we provide detailed vehicle history reports and thorough inspections on
                        all our used cars. We want you to have peace of mind when you purchase a vehicle from us,
                        knowing that you're getting a high-quality car that has been thoroughly vetted by our expert
                        technicians.
                    </li>
                    <li>We understand that buying a car is a big investment, which is why we offer a variety of
                        warranties and extended service plans to protect your investment and give you added peace of
                        mind. Our goal is to make your car buying experience as seamless and stress-free as possible, so
                        you can focus on enjoying your new ride.
                    </li>
                    <li>
                        Thank you for considering our car web store for your next vehicle purchase. We look forward to
                        helping you find the perfect car to fit your needs and budget.
                    </li>
                </ul>
            </article>
        </section>
    )
}

export default Hero