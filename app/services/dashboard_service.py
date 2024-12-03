
from app.database import db
from app.models.produtores import Produtor

class DashboardService:
    def get_dashboard_data(self):
        total_fazendas = db.session.query(Produtor).count()

        total_hectares = db.session.query(db.func.sum(Produtor.area_total)).scalar() or 0

        estados = db.session.query(
            Produtor.estado,
            db.func.count(Produtor.id).label('quantidade')
        ).group_by(Produtor.estado).all()

        culturas = db.session.query(Produtor.culturas).all()
        culturas = [cultura[0] if isinstance(cultura[0], str) else ','.join(cultura) for cultura in culturas]
        cultura_count = self._process_culturas(culturas)

        uso_solo = db.session.query(
            db.func.sum(Produtor.area_agricultavel).label('agricultavel'),
            db.func.sum(Produtor.area_vegetacao).label('vegetacao')
        ).first()
        
        return {
            "total_fazendas": total_fazendas,
            "total_hectares": total_hectares,
            "por_estado": [{"estado": e[0], "quantidade": e[1]} for e in estados],
            "por_cultura": cultura_count,
            "uso_solo": {
                "agricultavel": uso_solo.agricultavel or 0,
                "vegetacao": uso_solo.vegetacao or 0
            }
        }

    def _process_culturas(self, culturas):
        cultura_map = {}
        for cultura_list in culturas:
            for cultura in cultura_list[0].split(','):
                cultura = cultura.strip().lower()
                cultura_map[cultura] = cultura_map.get(cultura, 0) + 1
        return [{"cultura": k, "quantidade": v} for k, v in cultura_map.items()]
