from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from rehber.database import get_db, engine
from . import models, schemas

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Kişi ekle
@app.post("/rehber", response_model=schemas.RehberResponse, status_code=status.HTTP_201_CREATED)
def kisi_ekle(rehber: schemas.RehberCreate, db: Session = Depends(get_db)):
    yeni_kisi = models.Rehber(**rehber)
    db.add(yeni_kisi)
    db.commit()
    db.refresh(yeni_kisi)
    return yeni_kisi

# Kişileri listele
@app.get("/rehber", response_model=list[schemas.RehberResponse])
def kisileri_goruntule(db: Session = Depends(get_db)):
    kisiler = db.query(models.Rehber).all()
    return kisiler

# Kişi ara
@app.get("/rehber/{id}", response_model=schemas.RehberResponse)
def kisi_ara(id: int, db: Session = Depends(get_db)):
    kisi = db.query(models.Rehber).filter(models.Rehber.id == id).first()
    if kisi is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kişi bulunamadı.")
    return kisi

# Kişi sil
@app.delete("/rehber/{id}", status_code=status.HTTP_204_NO_CONTENT)
def kisi_sil(id: int, db: Session = Depends(get_db)):
    kisi = db.query(models.Rehber).filter(models.Rehber.id == id).first()
    if kisi is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kişi bulunamadı.")
    db.delete(kisi)
    db.commit()
    return {"detail": "Kişi silindi"}

#Kişi güncelle
@app.put("/rehber/{id}", response_model=schemas.RehberResponse)
def kisi_duzenle(id: int, rehber: schemas.RehberCreate, db: Session = Depends(get_db)):
    kisi = db.query(models.Rehber).filter(models.Rehber.id == id).first()
    if kisi is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kişi bulunamadı.")
    for key, value in rehber.dict().items():
        setattr(kisi, key, value)
    db.commit()
    db.refresh(kisi)
    return kisi


