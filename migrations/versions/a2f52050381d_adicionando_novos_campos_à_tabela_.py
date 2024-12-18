"""Adicionando novos campos à tabela produtores

Revision ID: a2f52050381d
Revises: 034485c4d12f
Create Date: 2024-11-25 21:41:39.300507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f52050381d'
down_revision = '034485c4d12f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produtores', schema=None) as batch_op:
        batch_op.alter_column('cpf_cnpj',
               existing_type=sa.VARCHAR(length=14),
               type_=sa.String(length=18),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produtores', schema=None) as batch_op:
        batch_op.alter_column('cpf_cnpj',
               existing_type=sa.String(length=18),
               type_=sa.VARCHAR(length=14),
               existing_nullable=False)

    # ### end Alembic commands ###
