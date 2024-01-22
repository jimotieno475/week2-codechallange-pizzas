import { useEffect, useState } from "react";

function Restaurants() {
    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        fetch("/restaurants")
            .then((r) => r.json())
            .then((restaurantsArray) => {
                setRestaurants(restaurantsArray );
            });
    }, []);

    return (
        <ul className="restaurants">
            {restaurants.map((restaurant) => (
                <li key={restaurant.id}>
                    <h3>{restaurant.name}</h3>
                    <p>{restaurant.address}</p>
                </li>
            ))}
        </ul>
    );

}

export default Restaurants;
