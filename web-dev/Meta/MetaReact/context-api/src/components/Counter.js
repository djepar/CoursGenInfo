import { useMealslistContext } from "../providers/MealsProvider";

const Counter = () => {
    const { meals } = useMealslistContext();

    return (
        <div>
            <h3>Number of meals today: {meals.length}</h3>
        </div>
    )
}

export default Counter;