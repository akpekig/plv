import '../styles/global.css';
import '@geoapify/geocoder-autocomplete/styles/minimal.css';
import { GeoapifyContext, GeoapifyGeocoderAutocomplete } from '@geoapify/react-geocoder-autocomplete';

const Home = () => {
    return (
        <GeoapifyContext apiKey="889fd4a0d01540c0ad6a296c4571f0e9">
            <header>
            </header>
            <main>
            <GeoapifyGeocoderAutocomplete
                placeholder="Enter address here"
                value={value}
                type={type}
                lang={language}
                position={position}
                countryCodes={countryCodes}
                limit={limit}
                filterByCountryCode={filterByCountryCode}
                filterByCircle={filterByCircle}
                filterByRect={filterByRect}
                filterByPlace={filterByPlace}
                biasByCountryCode={biasByCountryCode}
                biasByCircle={biasByCircle}
                biasByRect={biasByRect}
                biasByProximity={biasByProximity}
                placeSelect={onPlaceSelect}
                suggestionsChange={onSuggestionChange}
            />
            </main>
        </GeoapifyContext>
    )
}

export default Home