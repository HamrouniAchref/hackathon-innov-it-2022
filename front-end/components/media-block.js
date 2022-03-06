import { useState } from "react";
import Select from "react-select";

export default function MediaBlock({
  imageUrl,
  heading1,
  heading2,
  heading3,
  heading4,
  text1,
  text2,
  text3,
  text4,
  reverse,
}) {
  const [selectedOption, setselectedOption] = useState(null);

  return (
    <div className="flex-m mhn3-m mb4">
      <div className={`ph3-m w-50-m ${reverse && "order-last-m"}`}>
        <img src={imageUrl} alt="value image" className="db mb2" />
      </div>
      <div className="ph3-m w-50-m">
        <h3 className="f3 b lh-title mb1">{heading1}</h3>
        <p>{text1}</p>
      </div>
      <div className="ph3-m w-50-m">
        <h3 className="f3 b lh-title mb1">{heading2}</h3>
        <p>{text2}</p>
      </div>
      <div className="ph3-m w-50-m">
        <h3 className="f3 b lh-title mb1">{heading3}</h3>
        <Select
          value={selectedOption}
          placeholder="Selectionner l'etat"
          onChange={(selectedOption) => {
            setselectedOption(selectedOption);
          }}
          options={[
            { value: "Pas encore traiter", label: "Pas encore traiter" },
            {
              value: "En cours de la Reparation",
              label: "En cours de la Reparation",
            },
            { value: "Reparé", label: "Reparé" },
          ]}
          styles={{
            placeholder: (provided) => ({
              ...provided,
              color: "black",
              background: "#EBE7E6",
            }),
            option: (provided, state) => ({
              ...provided,
              background: "#EBE7E6",
              zIndex: 999,
            }),
          }}
        />
      </div>
      <div className="ph3-m w-50-m">
        <h3 className="f3 b lh-title mb1">{heading4}</h3>
        <div style={{ display: "flex" }}>
          <button
            style={{
              fontSize: "1rem",
              margin: "0.5rem",
              padding: "0.5rem",
              background: "#44ad44",
              color: "white",
            }}
          >
            Oui
          </button>
          <button
            style={{
              fontSize: "1rem",
              margin: "0.5rem",
              padding: "0.5rem",
              background: "red",
              color: "white",
            }}
          >
            Non
          </button>
        </div>
      </div>
    </div>
  );
}
