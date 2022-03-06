const PriceItem = ({ plan, price, description, items, id }) => (
  <div
    className="ph2"
    style={{
      borderRadius: "50%",
      border: "1px solid green",
      padding: "4rem",
    }}
  >
    <p className="primary f1 b tc lh-title center">
      {price}
      <span className="f4">{id === 1 ? "Dt" : "Kg"}</span>
    </p>
    <h3 className="b f5 grey-3 tc lh-title mb3">{plan}</h3>
  </div>
);

export default function Pricing({ heading, description, plans }) {
  return (
    <div className="bg-off-white pv4 ph3">
      <div className="mw7 center">
        <h2 className="f2 b lh-title mb3">{heading}</h2>
        <p className="mw6">{description}</p>
        <div
          className="flex-ns mhn2-ns mw7"
          style={{ justifyContent: "space-between", marginTop: "4rem" }}
        >
          {plans.map((p, index) => (
            <div className="w-33-ns ph2" key={p.plan}>
              <PriceItem
                id={index}
                plan={p.plan}
                price={p.price}
                description={p.description}
                items={p.items}
              />
            </div>
          ))}
        </div>
        <div
          style={{
            width: "100%",
            margin: "3rem auto",
            display: "flex",
            justifyContent: "center",
          }}
        >
          <button
            style={{
              fontSize: "1rem",
              margin: "0.5rem",
              padding: "1rem",
              background: "#44ad44",
              color: "white",
            }}
          >
            Prêt à échanger
          </button>
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div>
            <div className="mb3">
              <h2 className="f4 b lh-title">Nom:</h2>
              Ben Mubarak
            </div>
            <div className="mb3">
              <h2 className="f4 b lh-title ">Prénom:</h2>
              Anwar
            </div>
            <div className="mb3">
              <h2 className="f4 b lh-title ">Telephone:</h2>
              +216 55 555 555
            </div>
            <div className="mb3">
              <h2 className="f4 b lh-title ">Adresse:</h2>
              Technopole Mannouba, 2005, DCVF.
            </div>
            <div className="mb3">
              <h2 className="f4 b lh-title ">E-mail:</h2>
              mubarak.hosni@gmail.com
            </div>
          </div>
          <div style={{ border: "0.1rem solid green", borderRadius: "0.2rem" }}>
            <img alt="map" src="/img/screenmap.png" />
          </div>
        </div>
      </div>
    </div>
  );
}
